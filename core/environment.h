/**
 * This file is part of the "fviz" project
 *   Copyright (c) 2018 Paul Asmuth
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
#pragma once
#include <memory>
#include "return_code.h"
#include "color_scheme.h"
#include "graphics/measure.h"
#include "graphics/color.h"
#include "graphics/text.h"
#include "sexpr.h"
#include "element_factory.h"

namespace fviz {
class Layer;

struct Environment {
  Environment();
  Measure screen_width;
  Measure screen_height;
  double dpi;
  FontInfo font;
  Measure font_size;
  ColorScheme color_scheme;
  Color background_color;
  Color text_color;
  Color border_color;
  ElementMap element_map;
};

ReturnCode environment_setup_defaults(Environment* env);

} // namespace fviz

