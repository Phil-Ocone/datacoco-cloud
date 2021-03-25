# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.16] - 2021-03-22
### Changed
    - Added new class S3toS3Interaction
    - s3_to_s3_interaction: ability to copy files from S3 Account to Another
    - s3_to_s3_interaction: ability to move files from S3 Account to Another
    
## [0.1.15] - 2021-01-05
### Changed
    - Fix build conflicts

## [0.1.14] - 2020-12-11
### Changed
    - athena_interaction: Revert fix lint that produces error

## [0.1.13] - 2020-12-11
### Changed
    - athena_interaction: Fix 'sql' referenced before assignment

## [0.1.12] - 2020-12-10
### Changed
    - Fix dependencies with future==0.16.0

## [0.1.11] - 2020-12-10
### Changed
    - Fix dependencies with boto3 to >=1.9,<1.11

## [0.1.10] - 2020-08-05
### Changed
    - Set poll interval and max poll time for athena exec query

## [0.1.9] - 2020-03-18
### Changed
    - Support external package future minor versions

## [0.1.8] - 2020-03-10
### Changed
    - athena_interaction: Add "workgroup" parameters to repair_table() and run_existing_query()
    - Codacy fixes: update pylintrc, use isintance() instead of type()

## [0.1.7] - 2020-02-04
### Changed
    - Fix Flake8 linter
    - Fix emr interaction boto3 key parameter another typo

## [0.1.6] - 2020-02-04
### Changed
    - Fix emr interaction boto3 key parameter

## [0.1.5] - 2020-01-29
### Changed
    - Removed init functions in datacoco cloud classes

## [0.1.4] - 2020-01-28
### Changed
    - Removed initial module load in __init__.py

## [0.1.3] - 2020-01-25
### Changed
    - Readme.md to Readme.rst
### Added
    - Pull request template
    - Tox
    - Unit Tests

## [0.1.2] - 2020-01-23
### Added
    - Readme and contributing guidelines docs

## [0.1.1] - 2020-01-23
### Added
    - Jenkinsfile for CI/CD

## [0.1.0] - 2020-01-22
### Added
    - Datacoco cloud classes

[0.1.15]: https://github.com/equinoxfitness/datacoco-cloud/compare/v0.1.14...v0.1.15
[0.1.14]: https://github.com/equinoxfitness/datacoco-cloud/compare/v0.1.13...v0.1.14
[0.1.13]: https://github.com/equinoxfitness/datacoco-cloud/compare/v0.1.12...v0.1.13
[0.1.12]: https://github.com/equinoxfitness/datacoco-cloud/compare/v0.1.11...v0.1.12
[0.1.11]: https://github.com/equinoxfitness/datacoco-cloud/compare/v0.1.10...v0.1.11
[0.1.10]: https://github.com/equinoxfitness/datacoco-cloud/compare/v0.1.9...v0.1.10
[0.1.9]: https://github.com/equinoxfitness/datacoco-cloud/compare/v0.1.8...v0.1.9
[0.1.8]: https://github.com/equinoxfitness/datacoco-cloud/compare/v0.1.7...v0.1.8
[0.1.7]: https://github.com/equinoxfitness/datacoco-cloud/compare/v0.1.6...v0.1.7
[0.1.6]: https://github.com/equinoxfitness/datacoco-cloud/compare/v0.1.5...v0.1.6
[0.1.5]: https://github.com/equinoxfitness/datacoco-cloud/compare/v0.1.4...v0.1.5
[0.1.4]: https://github.com/equinoxfitness/datacoco-cloud/compare/v0.1.3...v0.1.4
[0.1.3]: https://github.com/equinoxfitness/datacoco-cloud/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/equinoxfitness/datacoco-cloud/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/equinoxfitness/datacoco-cloud/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/equinoxfitness/datacoco-cloud/releases/tag/v0.1.0
