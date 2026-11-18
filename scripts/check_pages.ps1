param(
    [string]$FilePath = 'd:\PTUDWNC\PTUDW-2026-Nhom25\test_cleaned.docx'
)
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open($FilePath)
$pages = $doc.ComputeStatistics(2)
$words = $doc.ComputeStatistics(0)
Write-Output "Pages: $pages"
Write-Output "Words: $words"
$doc.Close(0)
$word.Quit()
