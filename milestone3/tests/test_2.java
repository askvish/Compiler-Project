public class Scopes {
    // class-level variable
    int classVar = 1;

    public static void main(String[] args) {
        // method-level variable
        int methodVar = 2;

        // block-level variable
        {
            int blockVar = 3;
        }

        // demonstrate variable shadowing
        int classVar = 4;

    }
}
