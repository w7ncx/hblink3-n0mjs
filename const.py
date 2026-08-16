#!/usr/bin/env python
#
###############################################################################
#   Copyright (C) 2016-2018  Cortney T. Buffington, N0MJS <n0mjs@me.com>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
###############################################################################

'''
These are contants used by HBlink. Rather than stuff them into the main program
file, any new constants should be placed here. It makes them easier to keep track
of and keeps hblink.py shorter.
'''

__author__     = 'Cortney T. Buffington, N0MJS'
__copyright__  = 'Copyright (c) 2016 Cortney T. Buffington, N0MJS and the K0USY Group'
__credits__    = ''
__license__    = 'GNU GPLv3'
__maintainer__ = 'Cort Buffington, N0MJS'
__email__      = 'n0mjs@me.com'


# DMR Related constants
ID_MIN = 1
ID_MAX = 16776415

# Timers
STREAM_TO = .360
# Seconds of no audio after which a stream is declared ended. On RF, a gap this
# long means sync is lost and any resumption is a new stream (late entry), so the
# stream is over -- we time it out and emit an END.
STREAM_TIMEOUT = 2

# Options from the LC - used for late entry
LC_OPT = b'\x00\x00\x20'

# HomeBrew Protocol Frame Types
HBPF_VOICE      = 0x0
HBPF_VOICE_SYNC = 0x1
HBPF_DATA_SYNC  = 0x2
HBPF_SLT_VHEAD  = 0x1
HBPF_SLT_VTERM  = 0x2

# HomeBrew Protocol Commands
DMRA    = b'DMRA'
DMRC    = b'DMRC'
DMRD    = b'DMRD'
MSTCL   = b'MSTCL'
MSTNAK  = b'MSTNAK'
MSTPONG = b'MSTPONG'
MSTN    = b'MSTN'
MSTP    = b'MSTP'
MSTC    = b'MSTC'
RPTL    = b'RPTL'
RPTPING = b'RPTPING'
RPTCL   = b'RPTCL'
RPTACK  = b'RPTACK'
RPTK    = b'RPTK'
RPTC    = b'RPTC'
RPTP    = b'RPTP'
RPTA    = b'RPTA'
RPTO    = b'RPTO'


# Higheset peer ID permitted by HBP
PEER_MAX = 4294967295

# XLX reflector constants. These are protocol values, NOT configuration -- every
# XLX module presents as TS2/TG9 on the wire and there is no module identifier in
# any frame. xlxd hardcodes the same pair (DMRMMDVM_REFLECTOR_SLOT = DMR_SLOT2,
# and dstId 9 in cdmrmmdvmprotocol.cpp), as does DMRGateway (XLX_SLOT/XLX_TG at
# DMRGateway.cpp:57-58). The "TG 6" seen in hotspot documentation is DMRGateway's
# configurable RF-side talkgroup, which it rewrites to TG9 before transmitting --
# HBlink peers directly with xlxd, so TG9 is what we use. Never make these
# settable: a wrong value produces traffic xlxd silently discards, with no ACK,
# no module identity on the wire, and therefore no observable symptom.
XLX_TS   = 2
XLX_TGID = 9

# Module letter <-> reflector talkgroup. A-Z maps to 4001-4026; 4000 is UNLINK and
# is deliberately not a module.
XLX_UNLINK   = 4000
XLX_TG_BASE  = 4000
