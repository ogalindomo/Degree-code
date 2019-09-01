#include "lcdutils.h"
#include "shape.h"

typedef struct AbEye {
  void (*getBounds)(const struct AbEye *eye, const Vec2 *centerPos, Region *bounds);
  int  (*check)(const struct AbEye *eye, const Vec2 *centerPos, const Vec2 *pixel);
  const Vec2 size;
} AbEye;

int abEyeCheck(const AbEye *eye, const Vec2 *centerPos, const Vec2 *pixel){
  Region bounds;
void abEyeGetBounds(const AbEye *eye, const Vec2 *centerPos, Region *bounds);
  abEyeGetBounds(eye, centerPos, &bounds);
  //int position[] = pixel->axes;
  if((pixel->axes[0] >= centerPos->axes[0] - 3 && pixel->axes[0] <= centerPos->axes[0]+3) && (pixel->axes[1] >= centerPos->axes[1] - 3 && pixel->axes[1] <= centerPos->axes[1]+3))
    return 0;

  else if(((pixel->axes[1] <= centerPos->axes[1] - 5 && pixel->axes[1] >= centerPos->axes[1] - 10) || (pixel->axes[1] >= centerPos->axes[1] + 5 && pixel->axes[1] <= centerPos->axes[1] + 10)) && (pixel->axes[0] >= centerPos->axes[0]-5 && pixel->axes[0] <= centerPos->axes[0]+5))
  return 1;

  else if(((pixel->axes[0] <= centerPos->axes[0] - 5 && pixel->axes[0] >= centerPos->axes[0] - 10) || (pixel->axes[0] >= centerPos->axes[0] + 5 && pixel->axes[0] <= centerPos->axes[0] + 10)) && (pixel->axes[1] >= centerPos->axes[1]-10 && pixel->axes[1] <= centerPos->axes[1]+10))
  return 1;

  else if(((pixel->axes[0] <= centerPos->axes[0] - 11 && pixel->axes[0] >= centerPos->axes[0] - 13) || (pixel->axes[0] >= centerPos->axes[0] + 11 && pixel->axes[0] <= centerPos->axes[0] + 13 )) && (pixel->axes[1] >= centerPos->axes[1] - 7 && pixel->axes[1] <= centerPos->axes[1] + 7))
    return 1;

  else if(((pixel->axes[1] <= centerPos->axes[1] - 11 && pixel->axes[1] >= centerPos->axes[1] - 13) || (pixel->axes[1] >= centerPos->axes[1] + 11 && pixel->axes[1] <= centerPos->axes[1] + 13 )) && (pixel->axes[0] >= centerPos->axes[0] - 7 && pixel->axes[0] <= centerPos->axes[0] + 7))
    return 1;
  
  else
    return 0;
}

void abEyeGetBounds(const AbEye *eye, const Vec2 *centerPos, Region *bounds){
   vec2Sub(&bounds->topLeft, centerPos, &eye->size);
   vec2Add(&bounds->botRight, centerPos, &eye->size);
}

