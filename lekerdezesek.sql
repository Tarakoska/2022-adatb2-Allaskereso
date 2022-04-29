-- 24 órán belül jelentkezett valamilyen állásra álláskeresők neve
SELECT (VEZNEV || ' ' || KERNEV) as NEV FROM ((ALLASKERESO A
    INNER JOIN FELHASZNALO F ON F.ID = A.FEID)
    INNER JOIN JELENTKEZES J ON J.ALLID = A.ID)
    WHERE J.MIKOR > CURRENT_TIMESTAMP - interval '1' day;

-- Munkaadók felhasználóneve legalább 2 hírdetéssel
SELECT FELHNEV FROM (SELECT FELHNEV, COUNT(H.ID) as darab FROM ((MUNKAADO M
    INNER JOIN FELHASZNALO F on F.ID = M.FEID)
    LEFT JOIN HIRDETESFELADAS H ON H.MUID = M.ID)
    GROUP BY FELHNEV) WHERE darab > 1;

-- Álláskeresők neve legalább 1 szakmával
SELECT NEV FROM (SELECT (F.VEZNEV || ' ' || F.KERNEV) as NEV, COUNT(B.ALLID) as darab
    FROM ((ALLASKERESO A
    INNER JOIN FELHASZNALO F on F.ID = A.FEID)
    LEFT JOIN BIRTOKOL B on B.ALLID = A.ID)
    GROUP BY VEZNEV, KERNEV) WHERE darab > 0;