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
