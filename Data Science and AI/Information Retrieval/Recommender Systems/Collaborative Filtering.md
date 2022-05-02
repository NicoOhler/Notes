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
+ user based filtering
	+ assuming users A and B are similar
		+ similarity score needs to be above threshhold
	+ recommend items which A liked to B
		+ 
	+ ![[Pasted image 20220502172855.png]]
	+ ![[Pasted image 20220502173138.png]]
	+ 
+ item based filtering
	+  asssuming items x and y are similar
	+  if A liked x also recommend y

### Similarity Score
+ cosine similarity of user vectors
	+ does not account for different user rating tendencies
		+ some easily 10/10, some 8/10 at max
+ cosine similarity of centered user vectors
	+ normalize user ratings by each user's average rating value
	+ ![[Pasted image 20220502173535.png]]
	+ 

[[Recommender Systems]]
