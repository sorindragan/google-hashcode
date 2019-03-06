class Ride {
	
	Point start;
	Point finish;
	Point time;
	int startTime, finishTime;
	boolean taken;

	
	public String toString() {
		return "" + start + " " + finish + " "+ time;
	}
		
	public Ride(Point start, Point finish, int startTime, int finishTime) {
		this.start = start;
		this.finish = finish;
		this.startTime = startTime;
		this.finishTime = finishTime;
	}
}
