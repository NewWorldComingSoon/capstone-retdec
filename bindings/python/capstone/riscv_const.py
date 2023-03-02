# For Capstone Engine. AUTO-GENERATED FILE, DO NOT EDIT [riscv_const.py]

# Operand type for instruction's operands

RISCV_OP_INVALID = 0
RISCV_OP_REG = 1
RISCV_OP_IMM = 2
RISCV_OP_MEM = 3

# RISCV registers

RISCV_REG_INVALID = 0

# General purpose registers
RISCV_REG_X0 = 1
RISCV_REG_ZERO = RISCV_REG_X0
RISCV_REG_X1 = 2
RISCV_REG_RA = RISCV_REG_X1
RISCV_REG_X2 = 3
RISCV_REG_SP = RISCV_REG_X2
RISCV_REG_X3 = 4
RISCV_REG_GP = RISCV_REG_X3
RISCV_REG_X4 = 5
RISCV_REG_TP = RISCV_REG_X4
RISCV_REG_X5 = 6
RISCV_REG_T0 = RISCV_REG_X5
RISCV_REG_X6 = 7
RISCV_REG_T1 = RISCV_REG_X6
RISCV_REG_X7 = 8
RISCV_REG_T2 = RISCV_REG_X7
RISCV_REG_X8 = 9
RISCV_REG_S0 = RISCV_REG_X8
RISCV_REG_FP = RISCV_REG_X8
RISCV_REG_X9 = 10
RISCV_REG_S1 = RISCV_REG_X9
RISCV_REG_X10 = 11
RISCV_REG_A0 = RISCV_REG_X10
RISCV_REG_X11 = 12
RISCV_REG_A1 = RISCV_REG_X11
RISCV_REG_X12 = 13
RISCV_REG_A2 = RISCV_REG_X12
RISCV_REG_X13 = 14
RISCV_REG_A3 = RISCV_REG_X13
RISCV_REG_X14 = 15
RISCV_REG_A4 = RISCV_REG_X14
RISCV_REG_X15 = 16
RISCV_REG_A5 = RISCV_REG_X15
RISCV_REG_X16 = 17
RISCV_REG_A6 = RISCV_REG_X16
RISCV_REG_X17 = 18
RISCV_REG_A7 = RISCV_REG_X17
RISCV_REG_X18 = 19
RISCV_REG_S2 = RISCV_REG_X18
RISCV_REG_X19 = 20
RISCV_REG_S3 = RISCV_REG_X19
RISCV_REG_X20 = 21
RISCV_REG_S4 = RISCV_REG_X20
RISCV_REG_X21 = 22
RISCV_REG_S5 = RISCV_REG_X21
RISCV_REG_X22 = 23
RISCV_REG_S6 = RISCV_REG_X22
RISCV_REG_X23 = 24
RISCV_REG_S7 = RISCV_REG_X23
RISCV_REG_X24 = 25
RISCV_REG_S8 = RISCV_REG_X24
RISCV_REG_X25 = 26
RISCV_REG_S9 = RISCV_REG_X25
RISCV_REG_X26 = 27
RISCV_REG_S10 = RISCV_REG_X26
RISCV_REG_X27 = 28
RISCV_REG_S11 = RISCV_REG_X27
RISCV_REG_X28 = 29
RISCV_REG_T3 = RISCV_REG_X28
RISCV_REG_X29 = 30
RISCV_REG_T4 = RISCV_REG_X29
RISCV_REG_X30 = 31
RISCV_REG_T5 = RISCV_REG_X30
RISCV_REG_X31 = 32
RISCV_REG_T6 = RISCV_REG_X31

# Floating-point registers
RISCV_REG_F0_32 = 33
RISCV_REG_F0_64 = 34
RISCV_REG_F1_32 = 35
RISCV_REG_F1_64 = 36
RISCV_REG_F2_32 = 37
RISCV_REG_F2_64 = 38
RISCV_REG_F3_32 = 39
RISCV_REG_F3_64 = 40
RISCV_REG_F4_32 = 41
RISCV_REG_F4_64 = 42
RISCV_REG_F5_32 = 43
RISCV_REG_F5_64 = 44
RISCV_REG_F6_32 = 45
RISCV_REG_F6_64 = 46
RISCV_REG_F7_32 = 47
RISCV_REG_F7_64 = 48
RISCV_REG_F8_32 = 49
RISCV_REG_F8_64 = 50
RISCV_REG_F9_32 = 51
RISCV_REG_F9_64 = 52
RISCV_REG_F10_32 = 53
RISCV_REG_F10_64 = 54
RISCV_REG_F11_32 = 55
RISCV_REG_F11_64 = 56
RISCV_REG_F12_32 = 57
RISCV_REG_F12_64 = 58
RISCV_REG_F13_32 = 59
RISCV_REG_F13_64 = 60
RISCV_REG_F14_32 = 61
RISCV_REG_F14_64 = 62
RISCV_REG_F15_32 = 63
RISCV_REG_F15_64 = 64
RISCV_REG_F16_32 = 65
RISCV_REG_F16_64 = 66
RISCV_REG_F17_32 = 67
RISCV_REG_F17_64 = 68
RISCV_REG_F18_32 = 69
RISCV_REG_F18_64 = 70
RISCV_REG_F19_32 = 71
RISCV_REG_F19_64 = 72
RISCV_REG_F20_32 = 73
RISCV_REG_F20_64 = 74
RISCV_REG_F21_32 = 75
RISCV_REG_F21_64 = 76
RISCV_REG_F22_32 = 77
RISCV_REG_F22_64 = 78
RISCV_REG_F23_32 = 79
RISCV_REG_F23_64 = 80
RISCV_REG_F24_32 = 81
RISCV_REG_F24_64 = 82
RISCV_REG_F25_32 = 83
RISCV_REG_F25_64 = 84
RISCV_REG_F26_32 = 85
RISCV_REG_F26_64 = 86
RISCV_REG_F27_32 = 87
RISCV_REG_F27_64 = 88
RISCV_REG_F28_32 = 89
RISCV_REG_F28_64 = 90
RISCV_REG_F29_32 = 91
RISCV_REG_F29_64 = 92
RISCV_REG_F30_32 = 93
RISCV_REG_F30_64 = 94
RISCV_REG_F31_32 = 95
RISCV_REG_F31_64 = 96
RISCV_REG_ENDING = 97

# RISCV instruction

RISCV_INS_INVALID = 0
RISCV_INS_ADD = 1
RISCV_INS_ADDI = 2
RISCV_INS_ADDIW = 3
RISCV_INS_ADDW = 4
RISCV_INS_AMOADD_D = 5
RISCV_INS_AMOADD_D_AQ = 6
RISCV_INS_AMOADD_D_AQ_RL = 7
RISCV_INS_AMOADD_D_RL = 8
RISCV_INS_AMOADD_W = 9
RISCV_INS_AMOADD_W_AQ = 10
RISCV_INS_AMOADD_W_AQ_RL = 11
RISCV_INS_AMOADD_W_RL = 12
RISCV_INS_AMOAND_D = 13
RISCV_INS_AMOAND_D_AQ = 14
RISCV_INS_AMOAND_D_AQ_RL = 15
RISCV_INS_AMOAND_D_RL = 16
RISCV_INS_AMOAND_W = 17
RISCV_INS_AMOAND_W_AQ = 18
RISCV_INS_AMOAND_W_AQ_RL = 19
RISCV_INS_AMOAND_W_RL = 20
RISCV_INS_AMOMAXU_D = 21
RISCV_INS_AMOMAXU_D_AQ = 22
RISCV_INS_AMOMAXU_D_AQ_RL = 23
RISCV_INS_AMOMAXU_D_RL = 24
RISCV_INS_AMOMAXU_W = 25
RISCV_INS_AMOMAXU_W_AQ = 26
RISCV_INS_AMOMAXU_W_AQ_RL = 27
RISCV_INS_AMOMAXU_W_RL = 28
RISCV_INS_AMOMAX_D = 29
RISCV_INS_AMOMAX_D_AQ = 30
RISCV_INS_AMOMAX_D_AQ_RL = 31
RISCV_INS_AMOMAX_D_RL = 32
RISCV_INS_AMOMAX_W = 33
RISCV_INS_AMOMAX_W_AQ = 34
RISCV_INS_AMOMAX_W_AQ_RL = 35
RISCV_INS_AMOMAX_W_RL = 36
RISCV_INS_AMOMINU_D = 37
RISCV_INS_AMOMINU_D_AQ = 38
RISCV_INS_AMOMINU_D_AQ_RL = 39
RISCV_INS_AMOMINU_D_RL = 40
RISCV_INS_AMOMINU_W = 41
RISCV_INS_AMOMINU_W_AQ = 42
RISCV_INS_AMOMINU_W_AQ_RL = 43
RISCV_INS_AMOMINU_W_RL = 44
RISCV_INS_AMOMIN_D = 45
RISCV_INS_AMOMIN_D_AQ = 46
RISCV_INS_AMOMIN_D_AQ_RL = 47
RISCV_INS_AMOMIN_D_RL = 48
RISCV_INS_AMOMIN_W = 49
RISCV_INS_AMOMIN_W_AQ = 50
RISCV_INS_AMOMIN_W_AQ_RL = 51
RISCV_INS_AMOMIN_W_RL = 52
RISCV_INS_AMOOR_D = 53
RISCV_INS_AMOOR_D_AQ = 54
RISCV_INS_AMOOR_D_AQ_RL = 55
RISCV_INS_AMOOR_D_RL = 56
RISCV_INS_AMOOR_W = 57
RISCV_INS_AMOOR_W_AQ = 58
RISCV_INS_AMOOR_W_AQ_RL = 59
RISCV_INS_AMOOR_W_RL = 60
RISCV_INS_AMOSWAP_D = 61
RISCV_INS_AMOSWAP_D_AQ = 62
RISCV_INS_AMOSWAP_D_AQ_RL = 63
RISCV_INS_AMOSWAP_D_RL = 64
RISCV_INS_AMOSWAP_W = 65
RISCV_INS_AMOSWAP_W_AQ = 66
RISCV_INS_AMOSWAP_W_AQ_RL = 67
RISCV_INS_AMOSWAP_W_RL = 68
RISCV_INS_AMOXOR_D = 69
RISCV_INS_AMOXOR_D_AQ = 70
RISCV_INS_AMOXOR_D_AQ_RL = 71
RISCV_INS_AMOXOR_D_RL = 72
RISCV_INS_AMOXOR_W = 73
RISCV_INS_AMOXOR_W_AQ = 74
RISCV_INS_AMOXOR_W_AQ_RL = 75
RISCV_INS_AMOXOR_W_RL = 76
RISCV_INS_AND = 77
RISCV_INS_ANDI = 78
RISCV_INS_AUIPC = 79
RISCV_INS_BEQ = 80
RISCV_INS_BGE = 81
RISCV_INS_BGEU = 82
RISCV_INS_BLT = 83
RISCV_INS_BLTU = 84
RISCV_INS_BNE = 85
RISCV_INS_CSRRC = 86
RISCV_INS_CSRRCI = 87
RISCV_INS_CSRRS = 88
RISCV_INS_CSRRSI = 89
RISCV_INS_CSRRW = 90
RISCV_INS_CSRRWI = 91
RISCV_INS_C_ADD = 92
RISCV_INS_C_ADDI = 93
RISCV_INS_C_ADDI16SP = 94
RISCV_INS_C_ADDI4SPN = 95
RISCV_INS_C_ADDIW = 96
RISCV_INS_C_ADDW = 97
RISCV_INS_C_AND = 98
RISCV_INS_C_ANDI = 99
RISCV_INS_C_BEQZ = 100
RISCV_INS_C_BNEZ = 101
RISCV_INS_C_EBREAK = 102
RISCV_INS_C_FLD = 103
RISCV_INS_C_FLDSP = 104
RISCV_INS_C_FLW = 105
RISCV_INS_C_FLWSP = 106
RISCV_INS_C_FSD = 107
RISCV_INS_C_FSDSP = 108
RISCV_INS_C_FSW = 109
RISCV_INS_C_FSWSP = 110
RISCV_INS_C_J = 111
RISCV_INS_C_JAL = 112
RISCV_INS_C_JALR = 113
RISCV_INS_C_JR = 114
RISCV_INS_C_LD = 115
RISCV_INS_C_LDSP = 116
RISCV_INS_C_LI = 117
RISCV_INS_C_LUI = 118
RISCV_INS_C_LW = 119
RISCV_INS_C_LWSP = 120
RISCV_INS_C_MV = 121
RISCV_INS_C_NOP = 122
RISCV_INS_C_OR = 123
RISCV_INS_C_SD = 124
RISCV_INS_C_SDSP = 125
RISCV_INS_C_SLLI = 126
RISCV_INS_C_SRAI = 127
RISCV_INS_C_SRLI = 128
RISCV_INS_C_SUB = 129
RISCV_INS_C_SUBW = 130
RISCV_INS_C_SW = 131
RISCV_INS_C_SWSP = 132
RISCV_INS_C_UNIMP = 133
RISCV_INS_C_XOR = 134
RISCV_INS_DIV = 135
RISCV_INS_DIVU = 136
RISCV_INS_DIVUW = 137
RISCV_INS_DIVW = 138
RISCV_INS_EBREAK = 139
RISCV_INS_ECALL = 140
RISCV_INS_FADD_D = 141
RISCV_INS_FADD_S = 142
RISCV_INS_FCLASS_D = 143
RISCV_INS_FCLASS_S = 144
RISCV_INS_FCVT_D_L = 145
RISCV_INS_FCVT_D_LU = 146
RISCV_INS_FCVT_D_S = 147
RISCV_INS_FCVT_D_W = 148
RISCV_INS_FCVT_D_WU = 149
RISCV_INS_FCVT_LU_D = 150
RISCV_INS_FCVT_LU_S = 151
RISCV_INS_FCVT_L_D = 152
RISCV_INS_FCVT_L_S = 153
RISCV_INS_FCVT_S_D = 154
RISCV_INS_FCVT_S_L = 155
RISCV_INS_FCVT_S_LU = 156
RISCV_INS_FCVT_S_W = 157
RISCV_INS_FCVT_S_WU = 158
RISCV_INS_FCVT_WU_D = 159
RISCV_INS_FCVT_WU_S = 160
RISCV_INS_FCVT_W_D = 161
RISCV_INS_FCVT_W_S = 162
RISCV_INS_FDIV_D = 163
RISCV_INS_FDIV_S = 164
RISCV_INS_FENCE = 165
RISCV_INS_FENCE_I = 166
RISCV_INS_FENCE_TSO = 167
RISCV_INS_FEQ_D = 168
RISCV_INS_FEQ_S = 169
RISCV_INS_FLD = 170
RISCV_INS_FLE_D = 171
RISCV_INS_FLE_S = 172
RISCV_INS_FLT_D = 173
RISCV_INS_FLT_S = 174
RISCV_INS_FLW = 175
RISCV_INS_FMADD_D = 176
RISCV_INS_FMADD_S = 177
RISCV_INS_FMAX_D = 178
RISCV_INS_FMAX_S = 179
RISCV_INS_FMIN_D = 180
RISCV_INS_FMIN_S = 181
RISCV_INS_FMSUB_D = 182
RISCV_INS_FMSUB_S = 183
RISCV_INS_FMUL_D = 184
RISCV_INS_FMUL_S = 185
RISCV_INS_FMV_D_X = 186
RISCV_INS_FMV_W_X = 187
RISCV_INS_FMV_X_D = 188
RISCV_INS_FMV_X_W = 189
RISCV_INS_FNMADD_D = 190
RISCV_INS_FNMADD_S = 191
RISCV_INS_FNMSUB_D = 192
RISCV_INS_FNMSUB_S = 193
RISCV_INS_FSD = 194
RISCV_INS_FSGNJN_D = 195
RISCV_INS_FSGNJN_S = 196
RISCV_INS_FSGNJX_D = 197
RISCV_INS_FSGNJX_S = 198
RISCV_INS_FSGNJ_D = 199
RISCV_INS_FSGNJ_S = 200
RISCV_INS_FSQRT_D = 201
RISCV_INS_FSQRT_S = 202
RISCV_INS_FSUB_D = 203
RISCV_INS_FSUB_S = 204
RISCV_INS_FSW = 205
RISCV_INS_JAL = 206
RISCV_INS_JALR = 207
RISCV_INS_LB = 208
RISCV_INS_LBU = 209
RISCV_INS_LD = 210
RISCV_INS_LH = 211
RISCV_INS_LHU = 212
RISCV_INS_LR_D = 213
RISCV_INS_LR_D_AQ = 214
RISCV_INS_LR_D_AQ_RL = 215
RISCV_INS_LR_D_RL = 216
RISCV_INS_LR_W = 217
RISCV_INS_LR_W_AQ = 218
RISCV_INS_LR_W_AQ_RL = 219
RISCV_INS_LR_W_RL = 220
RISCV_INS_LUI = 221
RISCV_INS_LW = 222
RISCV_INS_LWU = 223
RISCV_INS_MRET = 224
RISCV_INS_MUL = 225
RISCV_INS_MULH = 226
RISCV_INS_MULHSU = 227
RISCV_INS_MULHU = 228
RISCV_INS_MULW = 229
RISCV_INS_OR = 230
RISCV_INS_ORI = 231
RISCV_INS_REM = 232
RISCV_INS_REMU = 233
RISCV_INS_REMUW = 234
RISCV_INS_REMW = 235
RISCV_INS_SB = 236
RISCV_INS_SC_D = 237
RISCV_INS_SC_D_AQ = 238
RISCV_INS_SC_D_AQ_RL = 239
RISCV_INS_SC_D_RL = 240
RISCV_INS_SC_W = 241
RISCV_INS_SC_W_AQ = 242
RISCV_INS_SC_W_AQ_RL = 243
RISCV_INS_SC_W_RL = 244
RISCV_INS_SD = 245
RISCV_INS_SFENCE_VMA = 246
RISCV_INS_SH = 247
RISCV_INS_SLL = 248
RISCV_INS_SLLI = 249
RISCV_INS_SLLIW = 250
RISCV_INS_SLLW = 251
RISCV_INS_SLT = 252
RISCV_INS_SLTI = 253
RISCV_INS_SLTIU = 254
RISCV_INS_SLTU = 255
RISCV_INS_SRA = 256
RISCV_INS_SRAI = 257
RISCV_INS_SRAIW = 258
RISCV_INS_SRAW = 259
RISCV_INS_SRET = 260
RISCV_INS_SRL = 261
RISCV_INS_SRLI = 262
RISCV_INS_SRLIW = 263
RISCV_INS_SRLW = 264
RISCV_INS_SUB = 265
RISCV_INS_SUBW = 266
RISCV_INS_SW = 267
RISCV_INS_UNIMP = 268
RISCV_INS_URET = 269
RISCV_INS_WFI = 270
RISCV_INS_XOR = 271
RISCV_INS_XORI = 272
RISCV_INS_ENDING = 273

# Group of RISCV instructions

RISCV_GRP_INVALID = 0
RISCV_GRP_JUMP = 1
RISCV_GRP_ISRV32 = 128
RISCV_GRP_ISRV64 = 129
RISCV_GRP_HASSTDEXTA = 130
RISCV_GRP_HASSTDEXTC = 131
RISCV_GRP_HASSTDEXTD = 132
RISCV_GRP_HASSTDEXTF = 133
RISCV_GRP_HASSTDEXTM = 134
RISCV_GRP_ISRVA = 135
RISCV_GRP_ISRVC = 136
RISCV_GRP_ISRVD = 137
RISCV_GRP_ISRVCD = 138
RISCV_GRP_ISRVF = 139
RISCV_GRP_ISRV32C = 140
RISCV_GRP_ISRV32CF = 141
RISCV_GRP_ISRVM = 142
RISCV_GRP_ISRV64A = 143
RISCV_GRP_ISRV64C = 144
RISCV_GRP_ISRV64D = 145
RISCV_GRP_ISRV64F = 146
RISCV_GRP_ISRV64M = 147
RISCV_GRP_ENDING = 148
