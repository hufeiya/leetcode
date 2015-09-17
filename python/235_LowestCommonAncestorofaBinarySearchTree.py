/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    int small,big;
    if (p->val <= q->val){
        small = p->val;
        big = q->val;
    }else{
        small = q->val;
        big = p->val;
    }
    while(! (small <= root->val && root->val <= big)){
        if(small <= root->val){
            root = root->left;
        }else{
            root = root->right;
        }
    }
    return root;
}
