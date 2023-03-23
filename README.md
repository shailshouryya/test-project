# Overview

This repository contains dummy projects in different programming languages to test how packaging works for that programming language.


## Programming language agnostic tools

### GPG

  - the easiest way to download and install GnuPG is to
    - navigate to the `GnuPG binary releases` section at https://gnupg.org/download/
    - select the application for your operating system and follow the download link
    - follow the instructions for verifying the download and installing the software for your operating system from there
  - if you want to download GnuPG and install from the source files
    - navigate to the `Source code releases` section at https://gnupg.org/download/
    - download GnuPG and install (may need to extract and/or unzip the source files first)
    - download Pinentry and install (may need to extract and/or unzip the source files first)
  - keep in mind
    - the setup process may vary depending on your operating system
    - the specific applications you get along with your GPG installation may vary depending your operating system and the bundle you select
      - recent distributions of `debian` come pre-installed with `gpg`
      - most GnuPG application bundles install a GUI to streamline the process of creating and managing keys
        - the GPG Suite installed with [Mac GPG](https://gpgtools.org/) comes with `gpg` (binary), GPG Keychain, GPG Mail, and Pinentry
        - [GnuPG for OS X](https://gnupg.org/download/) comes with `gpg` (binary) and Pinentry, but not with GPG Keychain nor GPG Mail
        - [Gpg4win](https://gpg4win.org/download.html) comes with GpgOL, GpgEX, GnuPG, Kleopatra and pinentry-qt (includes both `pinentry.exe` and `pinentry-w32.exe`, not sure which one is run by default)
        - the Simple installer for the current GnuPG for Windows (gnupg-w32-X.Y.Z_yyyymmdd.exe) comes with GnuPg and Pinentry (`pinentry-basic.exe`), but not with GpgOL, GpgEX, nor Kleopatra
- some potentially useful tutorials
  - targeted for Windows, but includes platform agnostic information (see the `Option B: Command Line` sections): [Setting Up GPG on Windows (The Easy Way)](https://www.git-tower.com/blog/setting-up-gpg-windows/)
  - targeted for macOS, but includes platform agnostic concepts about `gpg` and public/private keys ("private key" is also referred to as a "secret key"): [First steps - where do I start, where do I begin? (Setup GPGTools, Create a new key, Your first encrypted email)](https://gpgtools.tenderapp.com/kb/how-to/first-steps-where-do-i-start-where-do-i-begin-setup-gpgtools-create-a-new-key-your-first-encrypted-email)


## General Guidelines

## Version tag rules

- `git` enforces no restrictions on naming conventions for tags
  - `git` sorts tags in alphabetical order
- GitHub enforces no restrictions on naming conventions for tags either (and uses `git` under the hood), but is more nuanced with the tag sorting
  - it appears the releases page (github.com/yourusername/yourreponame/releases) and the tags page (github.com/yourusername/yourreponame/tags) sort the releases and tags, respectively,
    - in reverse chronological order [with the tag/commit date as the sort key, not the release date as the sort key](https://github.com/Shadowsocks-NET/QvStaticBuild/releases#discussioncomment-1728546) (so a tag/commit with a more recent date will appear before a tag/commit with an older date), **but when there is a tie** (multiple tags/commits have the same date), GitHub uses
      - semantic versioning as the tiebreaker when the tag uses a **valid** semantic versioning tag (starts with a digit or a lowercase `v` and follows the `MAJOR.MINOR.PATCH` format, where `MAJOR`, `MINOR`, and `PATCH` are decimal values between 0-9) with **only the first 3 numeric parts of the tag** ordered using semantic version ordering, and **the remaining part of the tag sorted in reverse alphabetical order**
        - NOTE that the reverse chronological order **uses the date** and **does not use the datetime** of the tag/commit (so 2 tags from the same date with different release times will still be tied)
        - NOTE that if there are multiple tags that use a valid semver tag **and** are released on the same date **and** have the same value for the first three numeric fields `MAJOR.MINOR.PATCH`, the sorting **will use reverse alphabetical order** using the rest of the tag/release name as the sort key and **not use the rules specified in number 10 under the "Semantic Versioning Specification (SemVer)" section** on the [Semantic Versioning 2.0.0](https://semver.org/) document
        - NOTE that an uppercase `v`, such as `V1.2.3`, does not qualify as a valid semantic versioning tag by this definition
      - reverse alphabetical order as the tiebreaker (so `tag-d` will appear before `tag-c`) when the tag uses an **invalid** semantic versioning tag (starts with anything **other than** a digit or a lowercase `v`)
  - example sort order (same order on both the [Tags page](https://github.com/shailshouryya/test-project/tags) and [Releases page](https://github.com/shailshouryya/test-project/releases):
```
# these are correctly sorted in reverse chronological order
0.0.2.post7-python
0.0.2.post6-python
0.0.2.post5-python
0.0.0.post0
0.0.0
0.0.2.post4-python
0.0.2.post3-python
0.0.2_post_2-python
0.0.2-post-1-python
0.0.2.post0-python
0.0.2-python
0.0.1-python
```
  - see the following references for more information:
    - GitHub REST API docs indicate the latest release on the releases page (github.com/yourusername/yourreponame/releases) uses the [the most recent non-prerelease, non-draft release, sorted by the created_at attribute. The created_at attribute is the date of the commit used for the release, and not the date when the release was drafted or published.](https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28#get-the-latest-release)
      - however, the SORTING of ALL the releases is more nuanced: GitHub currently uses [a mix of](https://github.com/Shadowsocks-NET/QvStaticBuild/releases#discussioncomment-4697709)) [Semver 2.0.0](https://semver.org/spec/v2.0.0.html) and [pep440](https://peps.python.org/pep-0440/)
      - seems to order tags in reverse chronological order ([with the tag/commit date as the sort key, not the release date as the sort key](https://github.com/Shadowsocks-NET/QvStaticBuild/releases#discussioncomment-1728546)), and when there is a tie (multiple releases on the same date), GitHub uses semantic versioning as the tiebreaker
        - [when the tag does not use semantic versioning (does not start with 'v' or a number)](https://github.com/community/community/discussions/8226#discussioncomment-1853768), uses [reverse alphabetical order](https://github.com/community/community/discussions/8226#discussioncomment-1982190) (so 'tag0' would come AFTER 'tag1' if both releases have the same date for their corresponding tag/commit linked to the release)
        - when the tag does use semantic versioning, only the first 3 numeric parts of a tag are used for the semantic version ordering, and then everything after is not parsed, and is sorted (reverse) alphabetically
          - [for `v4.10.0-alpha.3.10.geb2e56af` and `v4.10.0-alpha.3.9.ge0d22139`, semver only cares about the first 3 numeric parts (`v4.10.0`), and then everything after the `-` is not parsed and only sorted (reverse) alphabetically, so `3.10` appears below `3.9` because `1` comes before `9`.](https://github.com/Shadowsocks-NET/QvStaticBuild/releases#discussioncomment-4694630)
          - NOTE that if [the version starts with an upper case `V` (instead of a lower case `v`), the sorting falls back to string sorting. The version is only parsed as semver if the first character of the version is exactly the lower case `v`.]

- the `Compare` buttons on the [Releases page](https://github.com/shailshouryya/test-project/releases) seem to follow some entirely different order, with no obvious pattern:
```
# these are sorted in NEITHER reverse chronological order NOR reverse alphabetical order
0.0.2.post5-python
0.0.2.post4-python
0.0.2.post3-python
0.0.2_post_2-python   # this should be first if sorted reverse alphabetically
0.0.2.post0-python
0.0.2-python
0.0.2-post-1-python   # order after 0.0.2-python makes sense if reverse alphabetical order, but there are other inconsistencies for the reverse alphabetical sort (see comment above and below)
0.0.1-python
0.0.0                 # this should be LAST if sorted reverse alphabetically
0.0.0.post0
```
