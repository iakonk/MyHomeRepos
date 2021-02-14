A Social Network 
==================

Given a social network containing n members and a log 
file containing m timestamps at which times pairs of 
members formed friendships, design an algorithm to 
determine the earliest time at which all members are connected 
(i.e., every member is a friend of a friend of a friend … of a 
friend). Assume that the log file is sorted by timestamp and 
that friendship is an equivalence relation. The running time of
your algorithm should be mlogn or better and use extra space 
proportional to n.

**Answer:**
The earliest time at which all members are connected is when we 
union all into 1 connected component (1 tree). That 
means all the nodes in the tree have the same root.
This is an improvement of **weighted quick union** algorithm. 
Every time we call the union, we will check the weight of the 
tree to see whether it is equal to the size of n.