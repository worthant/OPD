import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Converter {
    public static void main(String[] args) {
        String inputFilename = "microCommandsVertical.txt";
        String outputFilename = "microCommandsHorizontal.txt";

        try (BufferedReader reader = new BufferedReader(new FileReader(inputFilename));
             BufferedWriter writer = new BufferedWriter(new FileWriter(outputFilename))) {

            String line;
            while ((line = reader.readLine()) != null) {
                writer.write("mw " + line + " ");
            }
        } catch (IOException e) {
            System.err.println("An error occurred while reading or writing the files:");
            e.printStackTrace();
        }
    }
}
