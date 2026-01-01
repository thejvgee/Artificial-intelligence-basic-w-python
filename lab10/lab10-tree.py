from treelib import Node,Tree

tree = Tree()

#өвөө
tree.create_node("Есүхэй баатар","Есүхэй баатар")

#хүү
tree.create_node("Тэмүгэ","Тэмүгэ",parent = "Есүхэй баатар")
tree.create_node("Тэмүүжин","Тэмүүжин",parent="Есүхэй баатар")

# ач 
tree.create_node("Зүчи","Зүчи", parent="Тэмүүжин")
tree.create_node("Өгөөдэй","Өгөөдэй", parent="Тэмүүжин")

#гуч
tree.create_node("Гүюүг","Гүюүг", parent="Өгөөдэй")

tree.show()