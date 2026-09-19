Add-Type -AssemblyName System.Drawing
 = Get-ChildItem '..\..\Desktop' | Where-Object { .Name -like '*입시분석*' } | Get-ChildItem | Where-Object { .Name -like '*논술*' } | Get-ChildItem -Filter '*.jpg'
foreach ( in ) {
     = 'scratch/' + .BaseName + '_rot.jpg'
    Write-Host .FullName
     = [System.Drawing.Image]::FromFile(.FullName)
    .RotateFlip([System.Drawing.RotateFlipType]::Rotate180FlipNone)
    .Save(, [System.Drawing.Imaging.ImageFormat]::Jpeg)
    .Dispose()
}
Write-Host 'ALL_DONE'