class Solution {
public:
  int bestTeamScore(vector<int> &scores, vector<int> &ages) {
    assert(scores.size() == ages.size());
    vector<pair<int, int>> vals;
    vals.reserve(ages.size());
    for (uint i = 0; i < ages.size(); ++i) {
      vals.emplace_back(ages[i], scores[i]);
    }
    sort(vals.begin(), vals.end(), greater<>());

    vector<int> dp(vals.size());
    for (uint i = 0; i < vals.size(); ++i) {
      int score = vals[i].second;
      dp[i] = score;
      for (uint j = 0; j < i; ++j) {
        if (score <= vals[j].second)
          dp[i] = max(dp[i], dp[j] + score);
      }
    }
    return *max_element(dp.begin(), dp.end());
  }
};
