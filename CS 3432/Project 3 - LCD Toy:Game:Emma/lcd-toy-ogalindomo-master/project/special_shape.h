#ifndef special_shape
#define special_shape
#include "shape.h"
#include "lcdutils.h"
#include "special_shape.c"


extern void abEyeGetBounds(const AbEye *eye, const Vec2 *centerPos, Region *bounds);

extern int abEyeCheck(const AbEye *eye, const Vec2 *centerPos, const Vec2 *pixel);

#endif
