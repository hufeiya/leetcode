class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }
        int count[26] = {0};
        for(int i = 0;i < s.length();i++){
            ++count[s[i] - 97];
        }
        for(int i = 0;i < s.length();i++){
            if(--count[t[i] - 97] < 0){
                return false;
            }
        }
        return true;
    }
};
