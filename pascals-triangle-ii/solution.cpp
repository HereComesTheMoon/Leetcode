class Solution {
public:
    std::vector<int> getRow(int rowIndex) {
        std::vector<int> row = std::vector<int>(rowIndex + 1);
        for( int i = 0; i <= rowIndex; ++i ) {
            row[i] = 1;
            for( int j = i - 1; 0 < j; --j ) {
                row[j] += row[j-1];
            }
        }

        return row;
    }
};
