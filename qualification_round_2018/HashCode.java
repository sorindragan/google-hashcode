import java.util.ArrayList;
import java.util.Comparator;
import java.util.PriorityQueue;

class Car {
	
	// variation parameters
	public static final float VAR_S = 1;
	public static final float VAR_T = 1;
	static int bonus;
	
	int x,y,distanceToFinish;
	float currentRideDistance;
	boolean taken;
	ArrayList<Integer> rides;
	int finishTime;
	
	public Car (int x, int y) {
		this.x = x;
		this.y = y;
		distanceToFinish = 0;
		finishTime = 0;
		rides = new ArrayList<Integer>();
	}
	
	public float calculateRide(Ride ride, int currentTime,int lin, int col) {
		float distance = Math.abs(ride.start.x - ride.finish.x) + Math.abs(ride.start.y - ride.finish.y);
		currentRideDistance = distance;
		if(currentTime + ride.start.x + ride.start.y <= ride.startTime) {
			distance = distance + bonus;
		}
		float distanceToTarget = Math.abs(x - ride.start.x) + Math.abs(ride.start.y - y);
		// feature scalling
		float  weight = VAR_S * (1/distance) + VAR_T * (distanceToTarget/(lin+col - 2));
		return weight;
	}
}





class HashCode {
	public void run(int T, int lin, int col, ArrayList<Car> cars,ArrayList<Ride> rides) {
		for(int time = 0; time < T; time++) {
			for(Car car : cars) {
				if(!car.taken) {
					Ride bestRide = null;
					int index = 0;
					int takenRides = 0;
					float bestScore = 0;
					for (int j = 0; j < rides.size(); j++) {
						if(!rides.get(j).taken) {
							// calculate the best ride
							float currentScore =  car.calculateRide(rides.get(j), time, lin, col);
							if(currentScore > bestScore) {
								bestRide = rides.get(j);
								index = j;
								bestScore = currentScore;
							}
						}
					}
					if (bestRide == null) {
						return;
					}
					bestRide.taken = true;
					car.taken = true;
					
					car.x = bestRide.finish.x;
					car.y = bestRide.finish.y;
					
					car.finishTime = time + Math.abs(bestRide.start.x - bestRide.finish.x) + Math.abs(bestRide.start.y - bestRide.finish.y);
					car.rides.add(index);
				}
				else {
					if(time == car.finishTime) {
						car.taken = false;
					}
				}
			}
		}
	}
}
