# cuahsi-ciroh-argo-s3-pipeline

[![Release](https://img.shields.io/github/v/release/sblack-usu/cuahsi-ciroh-argo-s3-pipeline)](https://img.shields.io/github/v/release/sblack-usu/cuahsi-ciroh-argo-s3-pipeline)
[![Build status](https://img.shields.io/github/actions/workflow/status/sblack-usu/cuahsi-ciroh-argo-s3-pipeline/main.yml?branch=main)](https://github.com/sblack-usu/cuahsi-ciroh-argo-s3-pipeline/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/sblack-usu/cuahsi-ciroh-argo-s3-pipeline/branch/main/graph/badge.svg)](https://codecov.io/gh/sblack-usu/cuahsi-ciroh-argo-s3-pipeline)
[![Commit activity](https://img.shields.io/github/commit-activity/m/sblack-usu/cuahsi-ciroh-argo-s3-pipeline)](https://img.shields.io/github/commit-activity/m/sblack-usu/cuahsi-ciroh-argo-s3-pipeline)
[![License](https://img.shields.io/github/license/sblack-usu/cuahsi-ciroh-argo-s3-pipeline)](https://img.shields.io/github/license/sblack-usu/cuahsi-ciroh-argo-s3-pipeline)

An example repository showing how to use DVC pipeline with CUAHSI Argo and S3 services

- **Github repository**: <https://github.com/sblack-usu/cuahsi-ciroh-argo-s3-pipeline/>
- **Documentation** <https://sblack-usu.github.io/cuahsi-ciroh-argo-s3-pipeline/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:sblack-usu/cuahsi-ciroh-argo-s3-pipeline.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

## Releasing a new version



---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
