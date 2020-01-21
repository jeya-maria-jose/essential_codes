ttp = np.sum((yval == 1))
        tp = np.sum((yHaT == 1) & (yval == 1))
        fp = np.sum((yHaT == 1) & (yval == 0))
        fn = np.sum((yHaT == 0) & (yval == 1))
        #print(tp,fp,fn)
        tot = tp+fp
        tot2 = tp+fn
        if tot==0 or tot2 ==0 or tp==0:
          if ttp ==0:
            f1_s = 0
          else:
            f1_s = 1
        else:
          precision = tp / (tp + fp);
          recall = tp / (tp + fn);
          f1_s = (2 * precision * recall) / (precision + recall);
          #print(f1_s)
