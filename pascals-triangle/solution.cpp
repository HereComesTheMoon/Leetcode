class Solution {
public:
    std::vector<std::vector<int>> generate(int numRows) {
        std::vector<std::vector<int>> rows;
        rows.reserve(numRows);
        for(int i = 0; i < numRows; ++i) {
            std::vector<int> row = std::vector<int>(i + 1);

            row[0] = 1;
            row.back() = 1;
            for(int j = 1; j < i; ++j) {
                row[j] = rows[i-1][j-1] + rows[i-1][j];
            }
            rows.push_back(row);
        }
        return rows;
    }
};
