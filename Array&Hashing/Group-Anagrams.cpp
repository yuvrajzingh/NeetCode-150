class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        int n = strs.size();
        unordered_map<string, vector<string>>mp;

        string temp;
        for(int i=0; i<n; i++){
            temp = strs[i];
            sort(strs[i].begin(), strs[i].end());
            mp[strs[i]].push_back(temp);
        }

        vector<vector<string>> result;

        for(auto it=mp.begin(); it!=mp.end(); it++){
            result.push_back(it->second);
        }

        return result;
    }
};