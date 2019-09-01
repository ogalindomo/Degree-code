 
public class Schedule {
  int[][] schedule;

  Schedule(int nRooms, int nTimeSlots) {
    schedule = new int[nRooms][nTimeSlots];
  }

  //Introduced to see the configuration of a schedule at run-time.//
  void print()
  {
     for(int i = 0; i < this.schedule.length; i++){
         for(int j = 0; j < this.schedule[i].length; j++){
             System.out.print(schedule[i][j]+" ");
         }
         System.out.println();
     }
  }
}
