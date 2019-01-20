a = document.getElementsByTagName('th')
for (i of a) { if (i.className.includes('prodDetSectionEntry')) { q.push(i) } }
z =q.find(x => x.innerText.includes('Sellers'))