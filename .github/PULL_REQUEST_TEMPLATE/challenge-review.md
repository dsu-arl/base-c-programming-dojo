Assignee Checklist:
- [ ] Mark yourself as the assignee if you are the one who worked on it
- [ ] Add the `new challenge` label if it's a new challenge, `edit challenge` if it's for an existing challenge
- [ ] Copy and paste pull request URL into PACE Teams channel for someone to review

Reviewer Checklist:
- [ ] Mark yourself as the reviewer
- [ ] Verify the branch in the pull request is being merged into the correct branch (`dev` for `feature` branches, `main` for `release` branches)
- [ ] Test the challenge in the [staging environment](http://pwncollege-staging.arl.madren.org/)
- [ ] Start a review and add comments of anything that needs to be changed or fixed
- [ ] `Approve` or `Request changes` when submitting the pull request review. If marking `Request changes`, add a comment summarizing why.
- [ ] If approving the pull request:
  - [ ] Squash and merge the commits
  - [ ] Delete the branch that was merged
  - [ ] Close the linked issue
- [ ] Add comment to pull request post in PACE Teams channel if it has been approved or if changes need to be made