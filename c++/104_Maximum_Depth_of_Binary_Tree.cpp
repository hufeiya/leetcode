/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
    int maxDep = 0;
    int currentDep = 0;
public:
    int maxDepth(TreeNode* root) {
        findMax(root);
        return maxDep;
    }
    
    void findMax(TreeNode* node){
        if(node == NULL){
            return;
        }
        currentDep++;
        if(node->left == NULL && node->right == NULL){
            maxDep = std::max(maxDep,currentDep);
        }
        else{
            if(node->left){
                findMax(node->left);
            }
            if(node->right){
                findMax(node->right);
            }
        }
        currentDep--;
    
    }
};
