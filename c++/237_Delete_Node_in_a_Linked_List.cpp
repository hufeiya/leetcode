/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        if(node && node->next){
            node->val = node->next->val;
            ListNode* tobeDel = node->next;
            node->next = node->next->next;
            delete tobeDel;
        }
    }
};
