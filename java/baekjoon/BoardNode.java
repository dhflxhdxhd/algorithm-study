package baekjoon;

class BoardNode {
    int row;
    int col;

    public BoardNode(int row, int col) {
        this.row = row;
        this.col = col;
    }

    @Override
    public String toString() {
        return "BoardNode{" +
                "row=" + row +
                ", col=" + col +
                '}';
    }
}