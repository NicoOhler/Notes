### Overview
+ assuming users A and B are similar
	+ similarity score needs to be above threshhold
+ recommend items which A liked to B
	+ ![](Pasted%20image%2020220502172855.png)
	+ ![](Pasted%20image%2020220502173138.png)

### Similarity Score
+ cosine similarity of user vectors
	+ does not account for different user rating tendencies
		+ some easily 10/10, some 8/10 at max
+ cosine similarity of centered user vectors
	+ normalize user ratings by each user's average rating value
	+ ![](Pasted%20image%2020220502173535.png)

### Prediction
+ ![](Pasted%20image%2020220502173805.png)
+ fine tuning via
	+ more similarity if users agree on controversial items
		+ controversial if high variance in ratings
		+ more weight of those items
	+ more weight to ratings of similar users
