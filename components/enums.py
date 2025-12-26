from django.db import models


class CPUSocket(models.TextChoices):
    # Early / pre-Pentium
    SOCKET_1 = "SOCKET_1", "Socket 1 (386)"
    SOCKET_2 = "SOCKET_2", "Socket 2 (386)"
    SOCKET_3 = "SOCKET_3", "Socket 3 (486)"

    # Pentium era
    SOCKET_4 = "SOCKET_4", "Socket 4 (Pentium)"
    SOCKET_5 = "SOCKET_5", "Socket 5 (Pentium)"
    SOCKET_7 = "SOCKET_7", "Socket 7 / Super Socket 7"

    # Slot CPUs
    SLOT_1 = "SLOT_1", "Slot 1"
    SLOT_A = "SLOT_A", "Slot A"

    # Early P4 / Athlon
    SOCKET_370 = "SOCKET_370", "Socket 370"
    SOCKET_423 = "SOCKET_423", "Socket 423"
    SOCKET_478 = "SOCKET_478", "Socket 478"
    SOCKET_A = "SOCKET_A", "Socket A (462)"

    # AMD 64 era
    SOCKET_754 = "SOCKET_754", "Socket 754"
    SOCKET_939 = "SOCKET_939", "Socket 939"
    SOCKET_AM2 = "SOCKET_AM2", "Socket AM2"
    SOCKET_AM2P = "SOCKET_AM2+", "Socket AM2+"
    SOCKET_AM3 = "SOCKET_AM3", "Socket AM3"

    # Intel Core era
    LGA_775 = "LGA_775", "LGA 775"
    LGA_1156 = "LGA_1156", "LGA 1156"
    LGA_1366 = "LGA_1366", "LGA 1366"

    # Catch-all
    OTHER = "OTHER", "Other / Proprietary"


class RAMType(models.TextChoices):
    # Early
    FPM = "FPM", "Fast Page Mode"
    EDO = "EDO", "EDO DRAM"

    # SDR
    SDR = "SDR", "SDR SDRAM"

    # DDR family
    DDR = "DDR", "DDR"
    DDR2 = "DDR2", "DDR2"
    DDR3 = "DDR3", "DDR3"
    DDR4 = "DDR4", "DDR4"

    # Rambus
    RDRAM = "RDRAM", "RDRAM (Rambus)"

    # Laptop / special
    SO_DIMM = "SO_DIMM", "SO-DIMM (generic)"

    # Catch-all
    OTHER = "OTHER", "Other"


class StorageInterface(models.TextChoices):
    # Pre-ATA
    ST506 = "ST506", "ST-506 / MFM / RLL"

    # ATA / IDE family
    FLOPPY = "FLOPPY", "Floppy"
    IDE = "IDE", "IDE / PATA"
    EIDE = "EIDE", "EIDE"
    ATA33 = "ATA33", "ATA-33"
    ATA66 = "ATA66", "ATA-66"
    ATA100 = "ATA100", "ATA-100"
    ATA133 = "ATA133", "ATA-133"

    # SCSI
    SCSI_1 = "SCSI_1", "SCSI-1"
    SCSI_2 = "SCSI_2", "SCSI-2"
    ULTRA_SCSI = "ULTRA_SCSI", "Ultra SCSI"
    U160 = "U160", "Ultra160"
    U320 = "U320", "Ultra320"

    # SATA
    SATA_1 = "SATA_1", "SATA I (1.5 Gbps)"
    SATA_2 = "SATA_2", "SATA II (3 Gbps)"
    SATA_3 = "SATA_3", "SATA III (6 Gbps)"

    # Modern (optional)
    NVME = "NVME", "NVMe (PCIe)"

    # External
    USB = "USB", "USB"
    FIREWIRE = "FIREWIRE", "FireWire (IEEE 1394)"

    # Catch-all
    OTHER = "OTHER", "Other"


class RemovableMedia(models.TextChoices):
    # Floppy drives
    FLOPPY_525 = "FLOPPY_525", '5.25" Floppy'
    FLOPPY_35 = "FLOPPY_325", '3.5" Floppy'
    LS120 = "LS120", "LS-120"

    # CD
    CD_ROM = "CD_ROM", "CD-ROM"
    CD_R = "CD_R", "CD-R"
    CD_RW = "CD_RW", "CD-RW"

    # DVD
    DVD_ROM = "DVD_ROM", "DVD-ROM"
    DVD_R = "DVD_R", "DVD-R"
    DVD_RW = "DVD_RW", "DVD-RW"
    DVD_RAM = "DVD_RAM", "DVD-RAM"
    DVD_PLUS_R = "DVD+R", "DVD+R"
    DVD_PLUS_RW = "DVD+RW", "DVD+RW"

    # Blu-ray (optional but useful)
    BD_ROM = "BD_ROM", "Blu-ray ROM"
    BD_R = "BD_R", "Blu-ray R"
    BD_RE = "BD_RE", "Blu-ray RE"

    # Catch-all
    OTHER = "OTHER", "Other"


class ExpansionBus(models.TextChoices):
    # Early / 8–16 bit
    ISA_8 = "ISA_8", "ISA (8-bit)"
    ISA_16 = "ISA_16", "ISA (16-bit)"

    # VESA Local Bus
    VLB = "VLB", "VESA Local Bus (VLB)"

    # PCI family
    PCI = "PCI", "PCI"
    PCI_X = "PCI_X", "PCI-X"

    # Accelerated Graphics Port
    AGP_1X = "AGP_1X", "AGP 1×"
    AGP_2X = "AGP_2X", "AGP 2×"
    AGP_4X = "AGP_4X", "AGP 4×"
    AGP_8X = "AGP_8X", "AGP 8×"

    # PCI Express
    PCIE_1 = "PCIE_1", "PCI Express 1.x"
    PCIE_2 = "PCIE_2", "PCI Express 2.x"
    PCIE_3 = "PCIE_3", "PCI Express 3.x"
    PCIE_4 = "PCIE_4", "PCI Express 4.x"

    # Laptop / specialty (rare but real)
    PCMCIA = "PCMCIA", "PCMCIA / PC Card"
    EXPRESSCARD = "EXPRESSCARD", "ExpressCard"

    # Proprietary / legacy
    MCA = "MCA", "Micro Channel Architecture (IBM)"
    EISA = "EISA", "EISA"

    OTHER = "OTHER", "Other / Proprietary"
