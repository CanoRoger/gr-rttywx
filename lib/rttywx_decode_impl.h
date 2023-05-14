/* -*- c++ -*- */
/*
 * Copyright 2023 Roger Cano.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_RTTYWX_RTTYWX_DECODE_IMPL_H
#define INCLUDED_RTTYWX_RTTYWX_DECODE_IMPL_H

#include <gnuradio/rttywx/rttywx_decode.h>
#include <rtty_rx.h>
#include <cstdio>

namespace gr {
  namespace rttywx {

    class rttywx_decode_impl : public rttywx_decode
    {
     private:
       	FILE* rawfile;
     	rtty_rx* nv;

     public:
      rttywx_decode_impl(int sampling_rate, const std::string filename, bool reverse);
      ~rttywx_decode_impl();

      // Where all the action really happens
      int work(
              int noutput_items,
              gr_vector_const_void_star &input_items,
              gr_vector_void_star &output_items
      );
    };

  } // namespace rttywx
} // namespace gr

#endif /* INCLUDED_RTTYWX_RTTYWX_DECODE_IMPL_H */
