$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open('d:\PTUDWNC\PTUDW-2026-Nhom25\Bao_Cao_Do_An_Nhom_25_Culinary_Blog.docx')
$pages = $doc.ComputeStatistics(2)
$words = $doc.ComputeStatistics(0)
Write-Output "Pages: $pages"
Write-Output "Words: $words"
$doc.Close(0)
$word.Quit()
