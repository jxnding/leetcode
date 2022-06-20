/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> ans_;
    Solution(){
    }
    
    void traverse(TreeNode* root){
        if (root->left){
            traverse(root->left);
        }
        ans_.push_back(root->val);
        if (root->right){
            traverse(root->right);
        }
    }
    
    vector<int> inorderTraversal(TreeNode* root) {
        if (!root){return {};}
        traverse(root);
        return ans_;
    }
};