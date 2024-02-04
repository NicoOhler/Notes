### Overview
+ asssuming items x and y are similar
	+ similarity score needs to be above threshhold
+  if A liked x also recommend y
+  ![](../../../z_images/Pasted%20image%2020220502174918.png)
+  interests might change over time

### Similarity Score
+ cosine similarity of item vectors
	+ does not account for different user rating tendencies
		+ some easily 10/10, some 8/10 at max
+ cosine similarity of centered item vectors
	+ normalize user ratings by each user's average rating value
	+ ![](../../../z_images/Pasted%20image%2020220502175140.png)

### Prediction
+ ![](../../../z_images/Pasted%20image%2020220502175336.png)
+ fine tuning via
	+ more similarity if users agree on controversial items
		+ controversial if high variance in ratings
		+ more weight of those items
	+ more weight to ratings of similar users