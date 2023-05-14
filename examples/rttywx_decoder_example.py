#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: HF RTTY weather decoder example
# Author: Roger Cano
# GNU Radio version: 3.10.1.1

from gnuradio import analog
import math
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import rttywx




class rttywx_decoder_example(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "HF RTTY weather decoder example", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.audio_rate = audio_rate = 8000

        ##################################################
        # Blocks
        ##################################################
        self.rttywx_rttywx_decode_0 = rttywx.rttywx_decode(8000, '', True)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=8000,
                decimation=audio_rate,
                taps=[],
                fractional_bw=0)
        self.gr_moving_average_xx_0_1_0 = blocks.moving_average_ff(int(1*audio_rate), 1.0/(1*audio_rate), int(audio_rate), 1)
        self.freq_xlating_fir_filter_xxx_0_3_0 = filter.freq_xlating_fir_filter_ccf(1, firdes.low_pass(1.0,audio_rate,1,2000), 2000, audio_rate)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/cano/Desktop/seaTTY/rttywx/examples/rtty.wav', True)
        self.blocks_vco_c_0_0 = blocks.vco_c(audio_rate, -2*3.14159*290/1.5, 1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_float*1)
        self.blocks_multiply_xx_2_0 = blocks.multiply_vcc(1)
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 32767)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.audio_sink_0 = audio.sink(audio_rate, 'pulse', True)
        self.analog_quadrature_demod_cf_0_0_1_0 = analog.quadrature_demod_cf(40.0/(48000/audio_rate))
        self.analog_agc3_xx_0 = analog.agc3_cc(1e-3, 1e-4, 0.3, 1.0, 1)
        self.analog_agc3_xx_0.set_max_gain(65536)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc3_xx_0, 0), (self.blocks_multiply_xx_2_0, 0))
        self.connect((self.analog_agc3_xx_0, 0), (self.freq_xlating_fir_filter_xxx_0_3_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0_0_1_0, 0), (self.gr_moving_average_xx_0_1_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.analog_agc3_xx_0, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.rttywx_rttywx_decode_0, 0))
        self.connect((self.blocks_multiply_xx_2_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_vco_c_0_0, 0), (self.blocks_multiply_xx_2_0, 1))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_3_0, 0), (self.analog_quadrature_demod_cf_0_0_1_0, 0))
        self.connect((self.gr_moving_average_xx_0_1_0, 0), (self.blocks_vco_c_0_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_float_to_short_0, 0))


    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.analog_quadrature_demod_cf_0_0_1_0.set_gain(40.0/(48000/self.audio_rate))
        self.freq_xlating_fir_filter_xxx_0_3_0.set_taps(firdes.low_pass(1.0,self.audio_rate,1,2000))
        self.gr_moving_average_xx_0_1_0.set_length_and_scale(int(1*self.audio_rate), 1.0/(1*self.audio_rate))




def main(top_block_cls=rttywx_decoder_example, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
