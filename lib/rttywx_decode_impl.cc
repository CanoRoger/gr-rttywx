/* -*- c++ -*- */
/*
 * Copyright 2023 Roger Cano.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#include <gnuradio/io_signature.h>
#include "rttywx_decode_impl.h"

namespace gr {
  namespace rttywx {
    using input_type = short;
    rttywx_decode::sptr
    rttywx_decode::make(int sampling_rate, const std::string filename, bool reverse)
    {
      return gnuradio::make_block_sptr<rttywx_decode_impl>(
        sampling_rate, filename, reverse);
    }


    /*
     * The private constructor
     */
    rttywx_decode_impl::rttywx_decode_impl(int sampling_rate, const std::string filename, bool reverse)
      : gr::sync_block("rttywx_decode",
              gr::io_signature::make(1, 1, sizeof(input_type)),
              gr::io_signature::make(0, 0, 0))
    {
	    if (filename.empty() || filename == "-") {
		rawfile = stdout;
	    } else {
		rawfile = fopen(filename.c_str(), "a");
	    }
	    // disable buffering on raw file
	    setvbuf(rawfile, nullptr, _IONBF, 0);
	    //printf("caca?");
	    nv = new rtty_rx(sampling_rate, false, reverse, rawfile); 
	    //printf("caca");
    }

    /*
     * Our virtual destructor.
     */
    rttywx_decode_impl::~rttywx_decode_impl()
    {
	    //delete nv;
	    //nv = nullptr;
	    if (rawfile != stdout)
		fclose(rawfile);
	    if (rawfile == stdout)
		setvbuf(rawfile, nullptr, _IOLBF, 0);
	    rawfile = nullptr;
    }

    int
    rttywx_decode_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      auto in = static_cast<const input_type*>(input_items[0]);
      nv->rx_process(in, noutput_items);
      //printf("putamerda");
      return noutput_items;
    }

  } /* namespace rttywx */
} /* namespace gr */
