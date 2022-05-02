# Collaborative Filtering
### Overview
+ recommandation based on user interactions with items in a system
	+ interactions such as
		+ user ratings
		+ clicks
		+ purchases

### Core Assumptions
+ two type of entities
	+ Users
	+ Items
+ interaction between users and items via online system
+ all user-item-interactions are tracked
	+ matrix entry

### Example
+ ![[Pasted image 20220502172300.png]]

### CF Techniques
+ [[User Based CF]]
	+ assuming users A and B are similar
		+ similarity score needs to be above threshhold
	+ recommend items which A liked to B
+ [[Item Based CF]]
	+  asssuming items x and y are similar
	+  if A liked x also recommend y

