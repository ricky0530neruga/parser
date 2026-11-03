"""
from bs4 import BeautifulSoup

html = 
<tr class="law">
    <td class="law-name">勞動基準法</td>
    <td class="count">98</td>
</tr>


result = soup.select_one("td.count")

print(result.get_text())
"""

from bs4 import BeautifulSoup

html = """
<div class="product">
    <h2 class="name">Subaru Outback</h2>
    <p class="price">1200000</p>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

result1 = soup.select_one("h2.name")
result2 = soup.select_one("p.price")

print(result1.get_text())
print(result2.get_text())