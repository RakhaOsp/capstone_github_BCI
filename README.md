This is capstone repository on the topic of ViT and BCI. Authors: Rakhat Ospanov and Shakhnazar Zhumabekov. 
The worked_try_mamba is succesfull implememntation of Mamba SSM with the use of CNN and MLP blocks. While the CNN is responsible for input space to feature space mapping and Spatial Convolution of the EEG data, MLP plays a crucial role as a classifier based on the output from Mamba.

Hard, mamba and Mamba_torch folders were used during the unsuccesfull attempt in Mamba pipeline in Windows system. Nevertheless, in our opinion this approach is still possible in the further work. For today the approach required the use of python 3.10 and custom wheels for causal-conv1d and trition in the base of windows operating system 

Dataset:

EEG Motor Movement/Imagery Dataset
https://physionet.org/content/eegmmidb/1.0.0/


Specifications:

  Code Style
  
      Language-Specific Guidelines:
          Python: Adhere to PEP 8 for code style.
          JavaScript: Follow Airbnb's JavaScript style guide.
          Java: Use Google's Java Style Guide.
  
      Formatting:
          Use 4 spaces for indentation.
          Limit lines to 80 characters.
          Include a blank line between functions and classes.
          Use meaningful names for variables and functions.
  
      Documentation:
          Document complex logic and decisions.
          Use docstrings for all public methods and classes.
          Ensure documentation is up-to-date with code changes.
  
  Commit Messages
  
      Format:
          Use the present tense: "Add feature" instead of "Added feature."
          Limit the subject line to 50 characters.
          Use the body to explain the "why" behind the change, not just "what."
  
      Structure:
  
      php
  
  <type>(<scope>): <subject>
  
  <body>
  
      Type: Type of change (e.g., feat, fix, chore, docs).
      Scope: A short description of the area of code affected (optional).
      Subject: A brief description of the change.
      Body: (Optional) A detailed explanation of the change.
  
  Example:
  
  sql
  
      feat(auth): add user login
  
      Implement user login functionality including validation and error handling.
  
      Types:
          feat: New feature for the user.
          fix: Bug fix.
          chore: Changes to the build process or auxiliary tools.
          docs: Documentation changes only.
  
  Branch Naming Conventions
  
      Format:
          Use lowercase with hyphens to separate words.
          Include a prefix that indicates the type of work (e.g., feature/, bugfix/, hotfix/).
  
      Examples:
          feature/user-authentication
          bugfix/login-error
          hotfix/critical-security-patch
  
      Branch Naming for Issues:
          Include the issue number if applicable: feature/issue-123-add-payment-method.
  
  Pull Request (PR) Processes
  
      Creating a Pull Request:
          Ensure your branch is up-to-date with the main branch.
          Provide a descriptive title and a detailed description of the changes.
          Reference any relevant issues (e.g., Fixes #123).
  
      Review Process:
          Assign at least one team member for review.
          Address all comments and feedback from reviewers.
          Ensure that all tests pass before merging.
  
      Merging:
          Use Squash and Merge to maintain a clean commit history.
          Do not merge if there are unresolved conflicts.
          Ensure all relevant documentation is updated before merging.
  
      After Merging:
          Delete the branch if it is no longer needed.
          Verify that the main branch is stable and functioning as expected.
  
  Additional Resources
  
      GitHub Flow
      Semantic Versioning
  
  If you have any questions or need clarification on any of these guidelines, please reach out to the project maintainers.
