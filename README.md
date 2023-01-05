# blockchain

This blockchain is made up of blocks that are constructed using a balanced Merkle tree. The hash function used in the Merkle tree is md5. Each non-leaf node's amount may change from tree to tree, but the number of children is fixed.

The first block's hash is calculated by taking the md5 hash of the concatenation of the initialization vector (IV) and the first block's TX root. The hash of the rest of the blocks is calculated by taking the md5 hash of the concatenation of the previous block's hash and the current block's TX root.

Example Balanced Merkle Trees

```
Height = 3, Sons = 2:
 
      TX root
       / \
      /   \
     /     \
   O        O
  / \      / \
 /   \    /   \
O     O  O     O
/|    /|  |\    |\
O O   O O  O O   O O
| |   | |  | |   | |
0 1   2 3  4 5   6 7
```


```
Height = 2, Sons = 3:


      TX root
       /|\
      / | \
     /  |  \
   O    |    O
  /|\   |   /|\
 / | \  |  / | \
O  O  O | O  O  O
|  |  | | |  |  |
0  1  2 | 6  7  8
       |
       O
      /|\
     / | \
    O  O  O
    |  |  |
    3  4  5
```
