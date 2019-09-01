#ifndef movement_module
#define movement_module
#include "shape.h"
#include "sr.h"

typedef struct MovLayer_s{
  Layer *layer;
  Vec2 velocity;
  struct MovLayer_s *next;
}MovLayer;

void movLayerDraw(MovLayer *movLayers, Layer *layers);

void mlAdvance(MovLayer *ml, Region *fence);
#endif
