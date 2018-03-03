import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;

public class Solution {
	public static void main(String args[]) throws IOException {
		int rows;
		int cols;
		int f;
		int n; //number of rides
		int b; //bonus
		int t; //number of steps
		String file = args[0];
		
		FileReader fr = new FileReader(file);
		BufferedReader br = new BufferedReader(fr);
		ArrayList<Ride> rides = new ArrayList();
		
		String line;
		
		line = br.readLine();
		String[] firstline = line.split(" ");
		rows = Integer.parseInt(firstline[0]);
		cols = Integer.parseInt(firstline[1]);
		f = Integer.parseInt(firstline[2]);
		n = Integer.parseInt(firstline[3]);
		b = Integer.parseInt(firstline[4]);
		t = Integer.parseInt(firstline[5]);
		
		for (int i = 0; i < n; i++) {
			line = br.readLine();
			String[] parsedline = line.split(" ");
			Ride ride = new Ride(new Point(Integer.parseInt(parsedline[0]), Integer.parseInt(parsedline[1])), 
						new Point(Integer.parseInt(parsedline[2]), Integer.parseInt(parsedline[3])),
						Integer.parseInt(parsedline[4]), Integer.parseInt(parsedline[5]));
			rides.add(ride);
		}
		
		ArrayList<Car> cars = new ArrayList<Car>(f);
		for (int i = 0; i < f; i++) {
			cars.add(new Car(0,0));
		}
		
		HashCode h = new HashCode();
		h.run(t, rows, cols, cars, rides);
		Car.bonus = b;
		for (int i = 0; i < f; i++) {
			System.out.print(cars.get(i).rides.size());
			System.out.print(" ");
			for (int j = 0; j < cars.get(i).rides.size(); j++) {
				System.out.print(cars.get(i).rides.get(j) + " ");
			}
			System.out.println();
		}
	}
}
