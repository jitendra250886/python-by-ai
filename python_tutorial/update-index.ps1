param(
  [switch]$Quiet
)
$ErrorActionPreference = 'Stop'
$root = Get-Location

function New-LocalIndex([string]$DirPath) {
  $files = Get-ChildItem -LiteralPath $DirPath -Filter *.md -File -ErrorAction SilentlyContinue | Sort-Object Name
  $lines = @(
    '# Documentation Index'
    ''
    'Below is an auto-generated list of Markdown files in this folder:'
    ''
  )
  foreach ($f in $files) {
    if ($f.Name -ieq 'INDEX.md' -or $f.Name -ieq 'FULL_COURSE_INDEX.md') { continue }
    $lines += "- [$($f.Name)]($($f.Name))"
  }
  $outPath = Join-Path $DirPath 'INDEX.md'
  Set-Content -LiteralPath $outPath -Value ($lines -join "`n") -Encoding utf8
}

# Root index
New-LocalIndex $root.Path

# Recursive full course index
$all = Get-ChildItem -Recurse -File -Filter *.md | Sort-Object FullName
$lines = @(
  '# Full Course Index'
  ''
  'Hierarchical list of all Markdown files under this folder (auto-generated).'
  ''
)
foreach ($f in $all) {
  if ($f.Name -ieq 'INDEX.md' -or $f.Name -ieq 'FULL_COURSE_INDEX.md') { continue }
  $rel = Resolve-Path -LiteralPath $f.FullName -Relative
  if (-not $rel.StartsWith('.')) { $rel = './' + $rel }
  $lines += "- [$rel]($rel)"
}
Set-Content -LiteralPath (Join-Path $root 'FULL_COURSE_INDEX.md') -Value ($lines -join "`n") -Encoding utf8

# Per-folder indices (including nested directories)
$dirs = Get-ChildItem -Recurse -Directory | Sort-Object FullName
foreach ($d in $dirs) { New-LocalIndex $d.FullName }

if (-not $Quiet) {
  Write-Host 'Regenerated INDEX.md, FULL_COURSE_INDEX.md, and per-folder INDEX.md files.' -ForegroundColor Green
}