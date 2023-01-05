
const size_t GRID_SIZE = 9;

class Solution {
public:
    bool isValidSudoku(const vector<vector<char>>& board) {
        for (size_t i = 0; i < GRID_SIZE; ++i) {
            auto row = vector<pair<int, int>>();
            auto col = vector<pair<int, int>>();
            auto box = vector<pair<int, int>>();
            row.reserve(GRID_SIZE);
            col.reserve(GRID_SIZE);
            box.reserve(GRID_SIZE);
            for (size_t j = 0; j < GRID_SIZE; ++j) {
                row.emplace_back(i, j);
                col.emplace_back(j, i);
                box.emplace_back((i / 3) * 3 + j / 3, (i % 3) * 3 + j % 3);
            }
                
            if (!isValid(board, row)) return false;
            if (!isValid(board, col)) return false;
            if (!isValid(board, box)) return false;
        }
    return true;    
    }

    bool isValid(const vector<vector<char>>& board, const vector<pair<int, int>>& indices) {
        auto seen = set<char>();
        uint count = 0;
        for (const auto& [i, j] : indices) {
            auto c = board[j][i];
            if (c == '.') continue;
            seen.insert(c);
            count++;
        }
        return count == seen.size();
    }
};