/* -*- c++ -*- */
/*
 * Copyright 2023 Roger Cano.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_RTTYWX_RTTYWX_DECODE_H
#define INCLUDED_RTTYWX_RTTYWX_DECODE_H

#include <gnuradio/rttywx/api.h>
#include <gnuradio/sync_block.h>
#include <rtty_rx.h>

namespace gr {
  namespace rttywx {

    /*!
     * \brief <+description of block+>
     * \ingroup rttywx
     *
     */
    class RTTYWX_API rttywx_decode : virtual public gr::sync_block
    {
     public:
      typedef std::shared_ptr<rttywx_decode> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of rttywx::rttywx_decode.
       *
       * To avoid accidental use of raw pointers, rttywx::rttywx_decode's
       * constructor is in a private implementation
       * class. rttywx::rttywx_decode::make is the public interface for
       * creating new instances.
       */
      static sptr make(int sampling_rate, const std::string filename, bool reverse);
    };

  } // namespace rttywx
} // namespace gr

#endif /* INCLUDED_RTTYWX_RTTYWX_DECODE_H */
