# Tungsten Examples

Example projects using the [Tungsten programming language](https://github.com/srmagura/Tungsten).

## How To

### Set up Tungsten CLI

These steps are for PowerShell (which is cross platform), but can be adapted for
bash, zsh, .etc.

1. Install PowerShell.
2. Clone the Tungsten repository and build it. This will produce an executable
   called `Tungsten.CLI.exe` (Windows) or `Tungsten.CLI` (Unix).
3. Copy `SetAliasTemplate.ps1` to `SetAlias.ps1` which is gitignored.
4. Edit `SetAlias.ps1` and put in the path to the `Tungsten.CLI` executable on
   your system.
5. In PowerShell, run `Import-Module SetAlias.ps1`. Now you can type `tungsten`
   to access the Tungsten CLI.

### Build & Run an Example

1. (Optional) Open the root folder of this repository in VS Code.
   `.vscode/settings.json` tells VS Code to treat `.w` files as Rust and
   `.wproj` files as JSON. Rust syntax highlighting does not work perfectly with
   Tungsten, but it is better than nothing.
2. `cd` to the directory of the example, e.g. `cd HelloWorld`.
3. Build the code by running `tungsten build`. You can optionally specify the
   project, e.g. `tungsten build HelloWorld.wproj`. This producs a DLL in the
   project's `bin` directory.
4. Run the code with `tungsten run`. Again, you can optionally specify the
   project, e.g. `tungsten run HelloWorld.wproj`.
