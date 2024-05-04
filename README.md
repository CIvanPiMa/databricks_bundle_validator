```shell
git init --initial-branch=main
git add README.md
git commit -m "Initial commit"

# The repo needs to exist already!
git remote add origin git@github.com:CIvanPiMa/databricks_bundle_validator.git
git push -u origin main

# Create and push the rest in a dev branch
git checkout -b feat/first-release
git add .
git commit -m "feat: Add initial project structure"
git push --set-upstream origin ${BRANCH_NAME}
```

# Databricks Bundle Validator

TBD
