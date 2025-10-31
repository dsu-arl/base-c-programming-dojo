<<<<<<< HEAD
import configparser
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
import os
import shutil
import subprocess
import yaml


class Dojo:
    def __init__(self):
        self.filepath = 'dojo.yml'
        self._data = None
        self.modules = []
    
    @property
    def data(self):
        if self._data is None:
            with open(self.filepath, 'r') as file:
                self._data = yaml.safe_load(file)
        if self._data is None:
            raise ValueError('Data is not set. Ensure dojo.yml file exists and is valid.')
        return self._data

    def write_yml(self):
        with open(self.filepath, 'w') as file:
            yaml.safe_dump(self.data, file, sort_keys=False, allow_unicode=True)

    def is_initialized(self):
        if os.path.exists(self.filepath):
            return True
        
        # Checks if repo contains any folders with module.yml file in them
        folders = [d for d in os.listdir() if os.path.isdir(d)]
        for folder in folders:
            filepath = os.path.join(folder, 'module.yml')
            if os.path.exists(filepath):
                return True

        return False

    def initialize(self, dojo_data):
        if self.is_initialized():
            print('Dojo is already initialized')
            return

        self._data = dojo_data
        self.write_yml()


class Module:
    def __init__(self, id=None) -> None:
        self.dojo = Dojo()
        self._id = id
        self._data = None
    
    @property
    def id(self):
        if self._id is None:
            raise ValueError('ID is not set.')
        return self._id

    @property
    def data(self):
        if self._data is None and self._id is not None:
            self.filepath = os.path.join(self.id, 'module.yml')
            with open(self.filepath, 'r') as file:
                self._data = yaml.safe_load(file)
        if self._data is None:
            raise ValueError('Data is not set. Ensure ID is set and file exists.')
        return self._data

    def write_yml(self) -> None:
        with open(self.filepath, 'w') as file:
            yaml.safe_dump(self.data, file, sort_keys=False)

    def create(self, module_data) -> None:
        module_path = module_data['id']
        module_name = module_data['name']
        self._id = module_data['id']

        # Create module directory
        try:
            print(f"Creating directory '{module_path}'...", end='', flush=True)
            os.makedirs(module_path)
            print(' Done')
        except FileExistsError:
            print(' Error')
            print(f"Directory '{module_path}' already exists")
        except Exception as e:
            print(' Error')
            print(f'An error occurred trying to create the folder: {e}')

        # Add to dojo.yml modules
        print('Adding module to dojo.yml file...', end='', flush=True)
        self.dojo.data['modules'].append(module_data)
        self.dojo.write_yml()
        print(' Done')

        # Create module.yml file
        print('Creating module.yml file...', end='', flush=True)
        filepath = os.path.join(module_path, 'module.yml')
        with open(filepath, 'w', encoding='utf-8') as file:
            yaml.safe_dump({'name': module_name, 'challenges': []}, file, sort_keys=False)
        print(' Done')

        # Create DESCRIPTION.md file
        print('Creating DESCRIPTION.md file...', end='', flush=True)
        filepath = os.path.join(module_path, 'DESCRIPTION.md')
        with open(filepath, 'w'):
            pass
        print(' Done')

    def delete(self) -> None:
        # Delete folder
        if os.path.exists(self.id):
            shutil.rmtree(self.id)
            # Remove from modules list in dojo.yml
            self.dojo.data['modules'] = [item for item in self.dojo.data['modules'] if item.get('id') != self.id]
            self.dojo.write_yml()


class Challenge:
    def __init__(self, module_id: str, challenge_id=None) -> None:
        self.module = Module(module_id)
        self._id = challenge_id
        self._data = None
    
    @property
    def id(self):
        if self._id is None:
            raise ValueError('ID is not set.')
        return self._id

    @property
    def data(self):
        if self._data is None and self._id is not None:
            self.filepath = os.path.join(self.module.id, 'module.yml')
            with open(self.filepath, 'r') as file:
                self._data = yaml.safe_load(file)
        if self._data is None:
            raise ValueError('Data is not set. Ensure ID is set and file exists.')
        return self._data

    def create(self, challenge_data):
        challenge_id = challenge_data['id']

        # Create challenge folder
        try:
            print(f"Creating directory '{challenge_id}'...", end='', flush=True)
            challenge_path = os.path.join(self.module.id, challenge_id)
            os.makedirs(challenge_path)
            print(' Done')
        except FileExistsError:
            print(' Error')
            print(f"Directory '{challenge_id}' already exists")
        except Exception as e:
            print(' Error')
            print(f'An error occurred trying to create the folder: {e}')

        # Create DESCRIPTION.md file
        print('Creating DESCRIPTION.md file...', end='', flush=True)
        filepath = os.path.join(challenge_path, 'DESCRIPTION.md')
        with open(filepath, 'w'):
            pass
        print(' Done')

        # Create verify file with the following content:
        '''
        #!/usr/bin/exec-suid -- /usr/bin/python3.12 -I
        import sys
        sys.path.append('/challenge')

        def print_flag():
            try:
                with open("/flag", "r") as f:
                    print(f.read())
            except FileNotFoundError:
                print("Error: Flag file not found.")

        # Add your imports and other code below here
        '''
        print('Creating verify file...', end='', flush=True)
        filepath = os.path.join(challenge_path, 'verify')
        # Make indents using 4 spaces instead of tabs
        indent = ' ' * 4
        with open(filepath, 'w') as file:
            file.write('#!/usr/bin/exec-suid -- /usr/bin/python3.12 -I\n')
            file.write("import sys\n")
            file.write("sys.path.append('/challenge')\n\n")
            file.write("def print_flag():\n")
            file.write(f"{indent}try:\n")
            file.write(f'{indent}{indent}with open("/flag", "r") as f:\n')
            file.write(f"{indent}{indent}{indent}print(f.read())\n")
            file.write(f"{indent}except FileNotFoundError:\n")
            file.write(f'{indent}{indent}print("Error: Flag file not found.")\n\n')
            file.write('# Add your imports and other code below here\n')
        print(' Done')

        # Add new challenge to module.yml file section
        if 'challenges' not in self.module.data:
            self.module.data['challenges'] = []
        self.module.data['challenges'].append(challenge_data)
        self.module.write_yml()

    def delete(self) -> None:
        self.module.data['challenges'] = [item for item in self.module.data['challenges'] if item.get('id') != self.id]
        challenge_path = os.path.join(self.module.id, self.id)
        if os.path.exists(challenge_path):
            self.delete_submodule('all')
            self.module.write_yml()
            shutil.rmtree(challenge_path)
        else:
            print('Challenge directory does not exist')

    def add_submodule(self, submodule_url: str, submodule_name: str) -> None:
        challenge_path = os.path.join(self.module.id, self.id)
        if not os.path.isdir(challenge_path):
            print(f"Challenge path '{challenge_path}' does not exist or is not a directory")
            return
        
        submodule_path = os.path.join(challenge_path, submodule_name)

        # Skip if the submodule folder already exists in the challenge
        if os.path.exists(submodule_path):
            print(f"Submodule '{submodule_name}' already exists in '{challenge_path}'")
            return

        # Add the submodule
        try:
            print(f"Adding submodule to '{challenge_path}'...")
            subprocess.run(['git', 'submodule', 'add', submodule_url, submodule_path], check=True)
            print('Done')
        except subprocess.CalledProcessError as e:
            print(f"Failed to add submodule to '{challenge_path}': {e}")

    def delete_submodule(self, submodule) -> None:
        challenge_path = os.path.join(self.module.id, self.id)
        if not os.path.isdir(challenge_path):
            print(f"Challenge path '{challenge_path}' does not exist or is not a directory")
            return
        
        # Get list of submodules in the challenge directory
        if submodule == 'all':
            submodules_to_delete = self.get_submodules()
        else:
            submodules_to_delete = [submodule]

        for submodule in submodules_to_delete:
            submodule_path = os.path.join(challenge_path, submodule)
            if not os.path.exists(submodule_path):
                print(f"Submodule '{submodule}' does not exist in '{challenge_path}'")
                return
            
            # Remove the submodule
            try:
                subprocess.run(['git', 'rm', '--cached', submodule_path], check=True)
                subprocess.run(['rm', '-rf', submodule_path], check=True)
                subprocess.run(['rm', '-rf', os.path.join('.git', 'modules', submodule_path)], check=True)
                print(f"Removed submodule from {challenge_path}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to delete submodule '{submodule}' from '{challenge_path}': {e}")

            # Remove submodule entry from .gitmodules file
            try:
                subprocess.run(['git', 'config', '--file', '.gitmodules', '--remove-section', f'submodule.{submodule_path}'], check=True)
                subprocess.run(['git', 'add', '.gitmodules'], check=True)
                print('Removed submodule entry from .gitmodules')
            except subprocess.CalledProcessError as e:
                print(f"Failed to remove submodule entry from .gitmodules: {e}")
    
    def get_submodules(self) -> list:
        # Returns a list of submodule names in the challenge directory
        gitmodules_file = '.gitmodules'
        if not os.path.exists(gitmodules_file):
            print(f"No .gitmodules file found in dojo repository.")
            return []
        
        try:
            config = configparser.ConfigParser()
            config.read(gitmodules_file)
        except Exception as e:
            print(f"Failed to read .gitmodules file: {e}")
            return []

        submodules = []
        for section in config.sections():
            if section.startswith(f'submodule "{self.module.id}/{self.id}') and config.has_option(section, 'path'):
                submodule_name = config.get(section, 'path').split('/')[-1]
                submodules.append(submodule_name)
        
        return submodules


class Menu:
    def __init__(self):
        self.dojo = Dojo()
        self.modules = []
    
    @staticmethod
    def _is_unique_new_entry(new, existing, type):
        new_id, new_name = new.get('id'), new.get('name')

        if new in existing:
            print(f"Error: A {type} with ID '{new_id}' and name '{new_name}' already exists.")
            return False
        
        for item in existing:
            if item.get('id') == new_id:
                print(f"Error: A {type} with ID '{new_id}' already exists.")
                return False
            elif item.get('name') == new_name:
                print(f"Error: A {type} with name '{new_name}' already exists.")
                return False

        return True

    def display(self):
        choices = [
            Choice(name='Edit Modules', value='module'),
            Choice(name='Edit Challenges', value='challenge'),
            Choice(name='Quit', value=None)
        ]

        if not self.dojo.is_initialized():
            choices = [
                Choice(name='Initialize Dojo', value=self._init_dojo),
                Choice(name='Quit', value=None)
            ]
        else:
            self.modules = [Choice(name=module['name'], value=module['id']) for module in self.dojo.data['modules']]
        
        choice = inquirer.rawlist(
            message='Choose an option:',
            choices=choices,
            default=1,
            vi_mode=True
        ).execute()

        if choice == 'module':
            choice = inquirer.rawlist(
                message='Choose a module option:',
                choices=[
                    Choice(name='Create', value=self._create_module),
                    Choice(name='Delete', value=self._delete_module),
                    Choice(name='Go Back', value=self.display)
                ],
                default=1,
                vi_mode=True
            ).execute()
        elif choice == 'challenge':
            choice = inquirer.rawlist(
                message='Choose a challenge option:',
                choices=[
                    Choice(name='Create', value=self._create_challenge),
                    Choice(name='Delete', value=self._delete_challenge),
                    Choice(name='Add Submodule', value=self._add_submodule_to_challenge),
                    Choice(name='Delete Submodule', value=self._delete_submodule_from_challenge),
                    Choice(name='Go Back', value=self.display)
                ],
                default=1,
                vi_mode=True
            ).execute()

        if choice:
            choice()

    def _init_dojo(self):
        dojo_name = inquirer.text(
            message='Enter dojo name (what will be displayed on pwn.college):'
        ).execute()
        dojo_id = dojo_name.lower().replace(' ', '-')

        dojo_type = inquirer.select(
            message='Enter dojo type:',
            choices=['Empty', 'Base', 'Class', 'Event', 'Custom'],
            default=1,
            vi_mode=True
        ).execute()
        if dojo_type == 'Custom':
            dojo_type = inquirer.text(
                message='Enter custom dojo type:',
                default=''
            ).execute()
        dojo_type = dojo_type.lower()

        # dojo_reward = inquirer.text(
        #     message='Enter dojo reward emoji:',
        # ).execute()

        confirm = inquirer.confirm(message='Do the dojo settings above look correct?').execute()

        if not confirm:
            print('Exiting dojo initialization')
            return
        
        dojo_data = {
            'id': dojo_id,
            'name': dojo_name,
            'modules': []
        }
        if dojo_type != 'empty':
            dojo_data['type'] = dojo_type
        
        print('Initializing dojo')
        self.dojo.initialize(dojo_data)

    def _create_module(self):
        module_name = inquirer.text(
            message='Enter module name (what will be displayed on pwn.college):'
        ).execute()
        module_path = module_name.lower().replace(' ', '-')
        new_module = {'id': module_path, 'name': module_name}

        # Need to make sure that module doesn't already exist in dojo.yml
        existing_modules = self.dojo.data['modules']
        while not self._is_unique_new_entry(new_module, existing_modules, type='module'):
            choice = inquirer.select(
                message="What would you like to do?",
                choices=['Try a different module name', 'Quit'],
                vi_mode=True
            ).execute()
            
            if choice == 'Quit':
                print('Exiting module creation process')
                return
        
            module_name = inquirer.text(
                message='Enter module name (what will be displayed on pwn.college):'
            ).execute()
            module_path = module_name.lower().replace(' ', '-')
            new_module = {'id': module_path, 'name': module_name}

        # Confirm that module name looks correct
        confirm = inquirer.confirm(message='Do the above settings look correct?').execute()
        if not confirm:
            print('Exiting module creation process')
            return

        Module().create(new_module)

    def _delete_module(self):
        # Deletes folder and removes from dojo.yml
        if len(self.modules) == 0:
            print('No modules in dojo to select from, exiting now')
            return

        # Display menu with module options
        module_choice = inquirer.select(
            message='Which module do you want to delete?',
            choices=self.modules,
            default=None,
            vi_mode=True
        ).execute()

        confirm = inquirer.confirm(
            message=f"Are you sure you want to delete the '{module_choice}' module?",
            default=False
        ).execute()

        if not confirm:
            print('Exiting delete module process')
            return
        
        Module(module_choice).delete()

    def _create_challenge(self):
        # Display menu with module options
        if len(self.modules) == 0:
            print('No modules in dojo to select from, exiting now')
            return

        module_choice = inquirer.rawlist(
            message='Which module are you adding this challenge to?',
            choices=self.modules,
            default=None,
            vi_mode=True
        ).execute()

        # Get challenge name from user and generate challenge id
        challenge_name = inquirer.text(
            message='Enter challenge name:'
        ).execute()

        default_challenge_id = challenge_name.lower().replace(' ', '-')
        challenge_id = inquirer.text(
            message='Enter challenge ID:',
            default=default_challenge_id
        ).execute()

        new_challenge = {'id': challenge_id, 'name': challenge_name, 'allow_privileged': False}

        challenge = Challenge(module_choice)

        # Need to make sure that challenge doesn't already exist in module.yml
        existing_challenges = challenge.module.data.get('challenges', [])
        while not self._is_unique_new_entry(new_challenge, existing_challenges, type='challenge'):
            choice = inquirer.select(
                message="What would you like to do?",
                choices=['Try a different challenge name', 'Quit'],
                vi_mode=True
            ).execute()
            
            if choice == 'Quit':
                print('Exiting challenge creation process')
                return
        
            challenge_name = inquirer.text(
                message='Enter challenge name:'
            ).execute()

            default_challenge_id = challenge_name.lower().replace(' ', '-')
            challenge_id = inquirer.text(
                message='Enter challenge ID:',
                default=default_challenge_id
            ).execute()

            new_challenge = {'id': challenge_id, 'name': challenge_name, 'allow_privileged': False}

        # Confirm that challenge name looks correct
        confirm = inquirer.confirm(message='Is the above information correct?').execute()

        if not confirm:
            print('Exiting challenge creation process')
            return

        challenge.create(new_challenge)
    
    def _delete_challenge(self):
        if len(self.modules) == 0:
            print('No modules in dojo to select from, exiting now')
            return

        module_choice = inquirer.rawlist(
            message='Which module do you want to delete the challenge from?',
            choices=self.modules,
            default=None,
            vi_mode=True
        ).execute()

        # Get the list of challenges
        module = Module(module_choice)
        existing_challenges = module.data.get('challenges', [])

        if len(existing_challenges) == 0:
            print(f"No challenges in '{module_choice}' module to delete, exiting now")
            return

        choices = [Choice(name=challenge['name'], value=(challenge['id'], challenge['name'])) for challenge in existing_challenges]
        choice = inquirer.select(
            message='Choose a challenge to delete:',
            choices=choices,
            default=None,
            vi_mode=True
        ).execute()
        challenge_id, challenge_name = choice

        confirm = inquirer.confirm(
            message=f"Are you sure you want to delete the challenge '{challenge_name}'",
        ).execute()

        if not confirm:
            print('Exiting challenge deletion process')
            return
        
        Challenge(module_choice, challenge_id).delete()
    
    def _add_submodule_to_challenge(self):
        # Display menu with module options
        if len(self.modules) == 0:
            print('No modules in dojo to select from, exiting now')
            return

        module_choice = inquirer.rawlist(
            message='Select module:',
            choices=self.modules,
            default=None,
            vi_mode=True
        ).execute()

        module = Module(module_choice)
        existing_challenges = module.data.get('challenges', [])
        challenge_choice = inquirer.rawlist(
            message='Select challenge:',
            choices=[Choice(name=challenge['name'], value=challenge['id']) for challenge in existing_challenges],
            default=None,
            vi_mode=True
        ).execute()

        submodule_url = inquirer.text(
            message='Enter submodule URL:'
        ).execute()
        default_submodule_name = submodule_url.split('/')[-1]
        submodule_name = inquirer.text(
            message='Enter submodule name:',
            default=default_submodule_name
        ).execute()

        # Confirm that challenge name looks correct
        confirm = inquirer.confirm(message='Is the above information correct?').execute()

        if not confirm:
            print('Exiting adding submodule to challenge process')
            return

        challenge = Challenge(module_choice, challenge_choice)
        challenge.add_submodule(submodule_url, submodule_name)

    def _delete_submodule_from_challenge(self):
        if len(self.modules) == 0:
            print('No modules in dojo to select from, exiting now')
            return

        module_choice = inquirer.rawlist(
            message='Select module:',
            choices=self.modules,
            default=None,
            vi_mode=True
        ).execute()

        module = Module(module_choice)
        existing_challenges = module.data.get('challenges', [])
        challenge_choice = inquirer.rawlist(
            message='Select challenge:',
            choices=[Choice(name=challenge['name'], value=challenge['id']) for challenge in existing_challenges],
            default=None,
            vi_mode=True
        ).execute()

        challenge = Challenge(module_choice, challenge_choice)
        submodules = challenge.get_submodules()

        submodule_choice = inquirer.rawlist(
            message='Select submodule to delete:',
            choices=[Choice(name='All', value='all')] + [Choice(name=submodule, value=submodule) for submodule in submodules],
            default=None,
            vi_mode=True
        ).execute()

        if submodule_choice == 'all':
            confirm_msg = f"Are you sure you want to delete ALL submodules in the '{challenge_choice}' challenge?"
        else:
            confirm_msg = f"Are you sure you want to delete the '{submodule_choice}' submodule in the '{challenge_choice}' challenge?"
        confirm = inquirer.confirm(message=confirm_msg).execute()

        if not confirm:
            print('Exiting submodule deletion process')
            return
        
        challenge.delete_submodule(submodule_choice)


if __name__ == '__main__':
    Menu().display()
=======
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
import os
import shutil
import subprocess
import yaml


######################### HELPER FUNCTIONS #########################
def read_dojo_yml():
    with open('dojo.yml', 'r') as file:
        dojo_data = yaml.safe_load(file)
    return dojo_data

def write_dojo_yml(dojo_data):
    with open('dojo.yml', 'w') as file:
        yaml.safe_dump(dojo_data, file, sort_keys=False, allow_unicode=True)

def read_module_yml(module_id):
    module_path = os.path.join(module_id, 'module.yml')
    with open(module_path, 'r') as file:
        module_data = yaml.safe_load(file)
    return module_data

def write_module_yml(module_id, data):
    module_path = os.path.join(module_id, 'module.yml')
    with open(module_path, 'w') as file:
        yaml.safe_dump(data, file, sort_keys=False)

def is_module(folder):
    module_path = os.path.join(folder, 'module.yml')
    return os.path.exists(module_path)

def get_all_modules():
    dojo_data = read_dojo_yml()
    modules = dojo_data['modules']

    all_modules = []
    for module in modules:
        all_modules.append({'name': module['name'], 'value': module['id']})

    return all_modules

def get_modules_for_menu():
    all_modules = get_all_modules()
    
    modules = []
    for module in all_modules:
        modules.append(Choice(
            name=module['name'],
            value=module['id']
        ))

    return modules

def add_submodule_to_dojo_module(module_folder, submodule_url, submodule_name):
    """
    Adds a submodule to every challenge in a dojo's module. Skips if submodule already exists in challenge

    :param module_folder: Path to the module folder containing the challenges
    :param submodule_url: URL of the submodule repository
    :param submodule_name: Name of the submodule
    """
    # Ensure module folder exists
    if not os.path.isdir(module_folder):
        print(f"Module folder '{module_folder}' does not exist")
        return
    
    # Iterate through each challenge in the module folder
    for challenge in os.listdir(module_folder):
        challenge_path = os.path.join(module_folder, challenge)

        # Check if it's a directory
        if os.path.isdir(challenge_path):
            submodule_path = os.path.join(challenge_path, submodule_name)

            # Skip if the submodule folder already exists in the challenge
            if os.path.exists(submodule_path):
                print(f"Submodule '{submodule_name}' already exists in '{challenge_path}', skipping")
                continue

            # Add the submodule
            try:
                print(f"Adding submodule to '{challenge_path}'...")
                subprocess.run(['git', 'submodule', 'add', submodule_url, submodule_path], check=True)
                print('Done')
            except subprocess.CalledProcessError as e:
                print(f"Failed to add submodule to '{challenge_path}': {e}")

def is_dojo_initalized():
    # Checks if dojo.yml file exists
    if os.path.exists('dojo.yml'):
        return True
    
    # Checks if repo contains any folders with module.yml file in them
    folders = [d for d in os.listdir() if os.path.isdir(d)]
    for folder in folders:
        filepath = os.path.join(folder, 'module.yml')
        if os.path.exists(filepath):
            return True

    return False

def is_unique_new_entry(new, existing, type):
    new_id, new_name = new.get('id'), new.get('name')

    if new in existing:
        print(f"Error: A {type} with ID '{new_id}' and name '{new_name}' already exists.")
        return False
    
    for item in existing:
        if item.get('id') == new_id:
            print(f"Error: A {type} with ID '{new_id}' already exists.")
            return False
        elif item.get('name') == new_name:
            print(f"Error: A {type} with name '{new_name}' already exists.")
            return False

    return True


######################### INITIALIZE DOJO #########################
def init_dojo():
    # Initializes dojo.yml file
    dojo_name = inquirer.text(
        message='Enter dojo name (what will be displayed on pwn.college):'
    ).execute()
    dojo_id = dojo_name.lower().replace(' ', '-')

    dojo_type = inquirer.text(
        message='Enter dojo type:',
        default='roadshow'
    ).execute()

    # dojo_reward = inquirer.text(
    #     message='Enter dojo reward emoji:',
    # ).execute()

    confirm = inquirer.confirm(message='Do the dojo settings above look correct?').execute()

    if not confirm:
        print('Exiting dojo initialization')
        return
    
    print('Initializing dojo')
    dojo_data = {
        'id': dojo_id,
        'name': dojo_name,
        'modules': []
    }
    if dojo_type != '':
        dojo_data['type'] = dojo_type
    write_dojo_yml(dojo_data)


######################### CREATE MODULE #########################
def create_module():
    # Open the dojo.yml file
    dojo_data = read_dojo_yml()

    module_name = inquirer.text(
        message='Enter module name (what will be displayed on pwn.college):'
    ).execute()
    module_path = module_name.lower().replace(' ', '-')
    new_module = {'id': module_path, 'name': module_name}

    # Need to make sure that module doesn't already exist in dojo.yml
    existing_modules = dojo_data['modules']
    while not is_unique_new_entry(new_module, existing_modules, type='module'):
        choice = inquirer.select(
            message="What would you like to do?",
            choices=['Try a different module name', 'Quit']
        ).execute()
        
        if choice == 'Quit':
            print('Exiting module creation process')
            return
    
        module_name = inquirer.text(
            message='Enter module name (what will be displayed on pwn.college):'
        ).execute()
        module_path = module_name.lower().replace(' ', '-')
        new_module = {'id': module_path, 'name': module_name}

    # Confirm that module name looks correct
    confirm = inquirer.confirm(message='Do the above settings look correct?').execute()
    if not confirm:
        print('Exiting module creation process')
        return

    # Create module directory
    try:
        print(f"Creating directory '{module_path}'...", end='', flush=True)
        os.makedirs(module_path)
        print(' Done')
    except FileExistsError:
        print(' Error')
        print(f"Directory '{module_path}' already exists")
    except Exception as e:
        print(' Error')
        print(f'An error occurred trying to create the folder: {e}')

    # Add to dojo.yml modules
    print('Adding module to dojo.yml file...', end='', flush=True)
    dojo_data['modules'].append(new_module)
    write_dojo_yml(dojo_data)
    print(' Done')

    # Create module.yml file
    print('Creating module.yml file...', end='', flush=True)
    filepath = os.path.join(module_path, 'module.yml')
    with open(filepath, 'w', encoding='utf-8') as file:
        yaml.safe_dump({'name': module_name}, file, sort_keys=False)
    print(' Done')

    # Create DESCRIPTION.md file
    print('Creating DESCRIPTION.md file...', end='', flush=True)
    filepath = os.path.join(module_path, 'DESCRIPTION.md')
    with open(filepath, 'w'):
        pass
    print(' Done')


######################### CREATE CHALLENGE #########################
def create_challenge():
    # Display menu with module options
    modules = get_all_modules()
    if len(modules) == 0:
        print('No modules in dojo to delete, exiting now')
        return

    module_choice = inquirer.rawlist(
        message='Which module are you adding this challenge to?',
        choices=modules,
        default=None
    ).execute()

    # Read module.yml file
    module_data = read_module_yml(module_choice)
    if 'challenges' not in module_data:
        module_data['challenges'] = []

    # Get challenge name from user and generate challenge id
    challenge_name = inquirer.text(
        message='Enter challenge name:'
    ).execute()

    default_challenge_id = challenge_name.lower().replace(' ', '-')
    challenge_id = inquirer.text(
        message='Enter challenge ID:',
        default=default_challenge_id
    ).execute()

    new_challenge = {'id': challenge_id, 'name': challenge_name, 'allow_privileged': False}

    # Need to make sure that challenge doesn't already exist in module.yml
    existing_challenges = module_data['challenges']
    while not is_unique_new_entry(new_challenge, existing_challenges, type='challenge'):
        choice = inquirer.select(
            message="What would you like to do?",
            choices=['Try a different challenge name', 'Quit']
        ).execute()
        
        if choice == 'Quit':
            print('Exiting challenge creation process')
            return
    
        challenge_name = inquirer.text(
            message='Enter challenge name:'
        ).execute()

        default_challenge_id = challenge_name.lower().replace(' ', '-')
        challenge_id = inquirer.text(
            message='Enter challenge ID:',
            default=default_challenge_id
        ).execute()

        new_challenge = {'id': challenge_id, 'name': challenge_name, 'allow_privileged': False}

    # Confirm that challenge name looks correct
    confirm = inquirer.confirm(message='Is the above information correct?').execute()

    if not confirm:
        print('Exiting challenge creation process')
        return

    # Create challenge folder
    try:
        print(f"Creating directory '{challenge_id}'...", end='', flush=True)
        module_path = os.path.join(module_choice, challenge_id)
        os.makedirs(module_path)
        print(' Done')
    except FileExistsError:
        print(' Error')
        print(f"Directory '{challenge_id}' already exists")
    except Exception as e:
        print(' Error')
        print(f'An error occurred trying to create the folder: {e}')

    # Create DESCRIPTION.md file
    print('Creating DESCRIPTION.md file...', end='', flush=True)
    filepath = os.path.join(module_path, 'DESCRIPTION.md')
    with open(filepath, 'w'):
        pass
    print(' Done')

    # Create verify file with the following content:
    '''
    #!/usr/bin/exec-suid --real -- /usr/bin/python -I
    import sys
    sys.path.append('/challenge')

    def print_flag():
        try:
            with open("/flag", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("Error: Flag file not found.")

    # Add your imports and other code below here
    '''
    print('Creating verify file...', end='', flush=True)
    filepath = os.path.join(module_path, 'verify')
    # Make indents using 4 spaces instead of tabs
    indent = ' ' * 4
    with open(filepath, 'w') as file:
        file.write('#!/usr/bin/exec-suid --real -- /usr/bin/python -I\n')
        file.write("import sys\n")
        file.write("sys.path.append('/challenge')\n\n")
        file.write("def print_flag():\n")
        file.write(f"{indent}try:\n")
        file.write(f'{indent}{indent}with open("/flag", "r") as f:\n')
        file.write(f"{indent}{indent}{indent}print(f.read())\n")
        file.write(f"{indent}except FileNotFoundError:\n")
        file.write(f'{indent}{indent}print("Error: Flag file not found.")\n\n')
        file.write('# Add your imports and other code below here\n')
    print(' Done')

    # Add new challenge to module.yml file section
    module_data['challenges'].append(new_challenge)
    write_module_yml(module_choice, module_data)


######################### DELETE MODULE #########################
def delete_module():
    # Deletes folder and removes from dojo.yml
    modules = get_all_modules()

    if len(modules) == 0:
        print('No modules in dojo to select from, exiting now')
        return

    # Display menu with module options
    module_choice = inquirer.rawlist(
        message='Which module do you want to delete?',
        choices=modules,
        default=None
    ).execute()

    confirm = inquirer.confirm(
        message=f"Are you sure you want to delete the '{module_choice}' module?",
        default=False
    ).execute()

    if not confirm:
        print('Exiting delete module process')
        return

    # Delete folder
    if os.path.exists(module_choice):
        shutil.rmtree(module_choice)
        # Remove from modules list in dojo.yml
        dojo_data = read_dojo_yml()
        dojo_data['modules'] = [item for item in dojo_data['modules'] if item.get('id') != module_choice]
        write_dojo_yml(dojo_data)


######################### DELETE CHALLENGE #########################
def delete_challenge():
    # Delete from challenges in module.yml
    # Delete challenge folder in module folder
    modules = get_all_modules()
    if len(modules) == 0:
        print('No modules in dojo to select from, exiting now')
        return

    module_choice = inquirer.rawlist(
        message='Which module do you want to delete the challenge from?',
        choices=modules,
        default=None
    ).execute()

    # Get the list of challenges
    module_info = read_module_yml(module_choice)
    challenges = module_info['challenges']

    if len(challenges) == 0:
        print(f"No challenges in '{module_choice}' module to delete, exiting now")
        return

    choices = []
    for challenge in challenges:
        choices.append(Choice(
            name=challenge['name'],
            value=(challenge['id'], challenge['name'])
        ))
    choice = inquirer.select(
        message='Choose a challenge to delete:',
        choices=choices,
        default=None
    ).execute()
    challenge_id, challenge_name = choice

    confirm = inquirer.confirm(
        message=f"Are you sure you want to delete the challenge '{challenge_name}'",
    ).execute()

    if not confirm:
        print('Exiting challenge deletion process')
        return

    module_info['challenges'] = [item for item in module_info['challenges'] if item.get('id') != challenge_id]
    challenge_path = os.path.join(module_choice, challenge_id)
    if os.path.exists(challenge_path):
        write_module_yml(module_choice, module_info)
        shutil.rmtree(challenge_path)
    else:
        print('Challenge directory does not exist')


######################### ADD SUBMODULE #########################
def add_submodule():
    modules = get_all_modules()
    if len(modules) == 0:
        print('No modules in dojo to select from, exiting now')
        return

    module_choice = inquirer.rawlist(
        message='Which module do you want to add the submodule to?',
        choices=modules,
        default=None
    ).execute()

    submodule_url = inquirer.text(
        message='Enter submodule URL:'
    ).execute()

    default_submodule_name = submodule_url.split('/')[-1]
    submodule_name = inquirer.text(
        message='Enter submodule name:',
        default=default_submodule_name
    ).execute()

    confirm = inquirer.confirm(
        message=f'Warning: This will add the submodule to every challenge in the {module_choice} module. Are you sure you want to proceed?'
    ).execute()

    if not confirm:
        print(f'Not adding submodule {submodule_name} to {module_choice} module')
        return
    
    print(f'Adding submodule {submodule_name} to {module_choice} module')
    add_submodule_to_dojo_module(module_choice, submodule_url, submodule_name)


######################### DISPLAY MENU #########################
def display_menu():
    choices = [
        Choice(name='Edit Modules', value='module'),
        Choice(name='Edit Challenges', value='challenge'),
        Choice(name='Quit', value=None)
    ]

    # Only display option to initialize if dojo.yml doesn't exist and no folders (modules) exist in repo
    initialized = is_dojo_initalized()
    if not initialized:
        choices.insert(0, Choice(name='Initialize Dojo', value=init_dojo))

    choice = inquirer.rawlist(
        message='Choose an option:',
        choices=choices,
        default=1
    ).execute()

    if choice == 'module':
        choice = inquirer.rawlist(
            message='Choose a module option:',
            choices=[
                Choice(name='Create', value=create_module),
                Choice(name='Add Submodule', value=add_submodule),
                Choice(name='Delete', value=delete_module),
                Choice(name='Go Back', value=display_menu)
            ],
            default=1
        ).execute()
    elif choice == 'challenge':
        choice = inquirer.rawlist(
            message='Choose a challenge option:',
            choices=[
                Choice(name='Create', value=create_challenge),
                Choice(name='Delete', value=delete_challenge),
                Choice(name='Go Back', value=display_menu)
            ],
            default=1
        ).execute()

    if choice:
        choice()


if __name__ == '__main__':
    display_menu()
>>>>>>> main
