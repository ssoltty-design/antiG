Add-Type -AssemblyName System.Drawing
$desktop = [System.Environment]::GetFolderPath('Desktop')
$dDir = Join-Path $desktop '입시분석 참고자료\논술일정표'
$files = Get-ChildItem $dDir -Filter "*.jpg"

foreach ($item in $files) {
    $outPath = Join-Path (Get-Location) ("scratch\" + $item.BaseName + "_rot.jpg")
    Write-Host "Rotating: " $item.Name
    $img = [System.Drawing.Image]::FromFile($item.FullName)
    $img.RotateFlip([System.Drawing.RotateFlipType]::Rotate180FlipNone)
    $img.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Jpeg)
    $img.Dispose()
}
Write-Host "ROTATION_COMPLETED"
