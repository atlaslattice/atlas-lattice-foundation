# GrokTools.psm1
# PowerShell module wrapper for grok CLI (lattice_cli + acn + MCP integration).
# Enables Copilot CLI (in PS sessions) to invoke grok commands natively.
# Part of maximal Windows + Copilot + grok interop.
# KRAKOA is home for all mutants.

function Invoke-Grok {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true, Position=0)]
        [string[]]$Args,

        [switch]$UseAcn
    )

    $habitat = $env:KRAKOA_HABITAT
    if (-not $habitat) {
        $habitat = "C:\Users\David Sheldon\OneDrive\Sheldonbrains\KRAKOA_Habitat"
    }

    $python = "python"
    if ($UseAcn) {
        $script = Join-Path $habitat "acn.py"
    } else {
        $script = Join-Path $habitat "Lattice\Krakoan_Machine_Language\lattice_cli.py"
    }

    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $python
    $psi.Arguments = "`"$script`" $($Args -join ' ')"
    $psi.WorkingDirectory = $habitat
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $true

    $p = [System.Diagnostics.Process]::Start($psi)
    $stdout = $p.StandardOutput.ReadToEnd()
    $stderr = $p.StandardError.ReadToEnd()
    $p.WaitForExit()

    [PSCustomObject]@{
        ExitCode = $p.ExitCode
        StdOut   = $stdout
        StdErr   = $stderr
        Command  = "$python $script $($Args -join ' ')"
    }
}

function Invoke-GrokCanonDiff {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)]
        [string]$Target
    )
    Invoke-Grok -Args @("canon", "diff", $Target)
}

function Invoke-GrokLatticeSlice {
    [CmdletBinding()]
    param(
        [int[]]$Providers,
        [int[]]$Capabilities,
        [int[]]$Lifecycles
    )
    $argsList = @("lattice", "slice")
    if ($Providers) { $argsList += "--providers"; $argsList += ($Providers -join ",")
    if ($Capabilities) { $argsList += "--capabilities"; $argsList += ($Capabilities -join ",")
    if ($Lifecycles) { $argsList += "--lifecycles"; $argsList += ($Lifecycles -join ",")
    Invoke-Grok -Args $argsList
}

function Invoke-GrokMgcpHabitat {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)]
        [ValidateSet("federate","teleport")]
        [string]$SubCmd,
        [string[]]$ExtraArgs
    )
    $argsList = @("mgcp", "habitat", $SubCmd)
    if ($ExtraArgs) { $argsList += $ExtraArgs }
    Invoke-Grok -Args $argsList
}

function Invoke-RunCliCommand {
    <#
    .SYNOPSIS
    Securely execute an allowlisted CLI via the Python SecureCLIRunner bridge (cli_runner.py).
    Implements the CLI Tool Execution Bridge for Windows/Copilot: structured result, no shell=True.
    Mirrors the MCP run_cli_command tool. "KRAKOA home for all mutants".
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)]
        [ValidateSet("grok","lattice","acn","gemini")]
        [string]$CommandName,

        [Parameter(Mandatory=$true)]
        [string[]]$Arguments
    )

    $habitat = $env:KRAKOA_HABITAT
    if (-not $habitat) {
        $habitat = "C:\Users\David Sheldon\OneDrive\Sheldonbrains\KRAKOA_Habitat"
    }

    $python = "python"
    $runnerScript = Join-Path $habitat "Canon_Implementation\MCP\cli_runner.py"

    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $python
    # Use the 'run' subcommand supported by cli_runner __main__ for direct bridge invocation
    $argString = "run $CommandName " + ($Arguments -join ' ')
    $psi.Arguments = "`"$runnerScript`" $argString"
    $psi.WorkingDirectory = $habitat
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $true

    $p = [System.Diagnostics.Process]::Start($psi)
    $stdout = $p.StandardOutput.ReadToEnd()
    $stderr = $p.StandardError.ReadToEnd()
    $p.WaitForExit()

    $parsed = $null
    try { $parsed = $stdout | ConvertFrom-Json } catch { }

    [PSCustomObject]@{
        ExitCode = $p.ExitCode
        StdOut   = $stdout
        StdErr   = $stderr
        Result   = $parsed
        Command  = "$python $runnerScript run $CommandName $($Arguments -join ' ')"
        Note     = "Via SecureCLIRunner (asyncio.create_subprocess_exec, allowlist, structured dict). Part of Gemini/Copilot/Grok interop."
    }
}

Export-ModuleMember -Function Invoke-Grok, Invoke-GrokCanonDiff, Invoke-GrokLatticeSlice, Invoke-GrokMgcpHabitat, Invoke-RunCliCommand
